import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader
from torchtext import datasets
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator


# Define a simple neural network classifier
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        x = torch.sigmoid(self.fc(x))
        return x


# Define tokenizer
tokenizer = get_tokenizer('spacy', language='en_core_web_sm')

# Define TabularDataset
train_data, test_data = datasets.ta(
    path='asg1_train.csv', format='csv', fields=[('text', 'text'), ('label', 'label')]), \
    TabularDataset(
        path='asg1_test.csv', format='csv', fields=[('text', 'text'), ('label', 'label')])


# Build vocab and load pre-trained word embeddings
def yield_tokens(data_iter):
    for _, text in data_iter:
        yield tokenizer(text)


vocab = build_vocab_from_iterator(yield_tokens(train_data), specials=["<unk>"])
vocab.load_vectors("glove.6B.100d")
vocab.set_default_index(vocab["<unk>"])


# Define collate function for DataLoader
def collate_batch(batch):
    label_list, text_list = [], []
    for (_label, _text) in batch:
        label_list.append(float(_label))
        processed_text = torch.tensor(vocab(tokenizer(_text)))
        text_list.append(processed_text)
    return torch.tensor(label_list), pad_sequence(text_list, padding_value=1.0)


# Define dataloader
train_loader = DataLoader(train_data, batch_size=64, shuffle=False, collate_fn=collate_batch)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False, collate_fn=collate_batch)

# Define model, loss function, and optimizer
input_size = len(vocab)
output_size = 1
model = NeuralNetwork(input_size, output_size)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
num_epochs = 5
for epoch in range(num_epochs):
    for labels, texts in train_loader:
        optimizer.zero_grad()
        outputs = model(texts).squeeze(1)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# Evaluate the model
test_loss = 0
test_acc = 0
model.eval()
with torch.no_grad():
    for labels, texts in test_loader:
        outputs = model(texts).squeeze(1)
        loss = criterion(outputs, labels)
        test_loss += loss.item()
        test_acc += (torch.round(torch.sigmoid(outputs)) == labels).sum().item()

print(f'Test Loss: {test_loss / len(test_loader):.3f} | Test Acc: {test_acc / len(test_loader):.2f}%')
