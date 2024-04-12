import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

# Define tokenizer
try:
    tokenizer = get_tokenizer('spacy', language='en_core_web_sm')
except OSError:
    print(
        "The 'en_core_web_sm' model is not installed. Please install it by running 'python -m spacy download en_core_web_sm' in your terminal."
    )
    # Handle the error appropriately here, e.g., by exiting the program or falling back to a different tokenizer.
train_data = pd.read_csv('./asg1_train.csv')


class NeuralNetwork(nn.Module):
    """A simple neural network classifier.

    Attributes:
        fc: A fully connected layer that takes input_size and outputs output_size.
    """

    def __init__(self, input_size, output_size):
        """Inits NeuralNetwork with input and output size."""
        super(NeuralNetwork, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        """Defines the computation performed at every call.

        Args:
            x: The input data.

        Returns:
            The sigmoid activation of the fully connected layer.
        """
        x = torch.sigmoid(self.fc(x))
        return x


class CustomDataset(Dataset):
    """Custom Dataset for loading and preprocessing data.

    Attributes:
        texts: A list of texts.
        labels: A list of corresponding labels.
        vectorizer: A CountVectorizer object.
        label_encoder: A LabelEncoder object.
    """

    def __init__(self, texts, labels, vectorizer, label_encoder):
        """Inits CustomDataset with texts, labels, vectorizer, and label_encoder."""
        self.texts = texts
        self.labels = labels
        self.vectorizer = vectorizer
        self.label_encoder = label_encoder

    def __len__(self):
        """Returns the total number of texts."""
        return len(self.texts)

    def __getitem__(self, idx):
        """Fetches a single item from the dataset.

        Args:
            idx: The index of the item.

        Returns:
            A tuple containing the vectorized text and the encoded label.
        """
        text = self.texts[idx]
        label = self.labels[idx]
        text_vec = self.vectorizer.transform([text]).toarray().squeeze()
        label_encoded = self.label_encoder.transform([label]).flatten()[0]
        return text_vec, label_encoded


# Build vocab and load pre-trained word embeddings
def yield_tokens(data_iter):
    for _, text in data_iter:
        yield get_tokenizer(text, 'en_core_web_lg')


vocab = build_vocab_from_iterator(yield_tokens(train_data), specials=['<unk>'])
vocab.load_vectors('glove.6B.100d')
vocab.set_default_index(vocab['<unk>'])


def collate_batch(batch):
    label_list, text_list = [], []
    for _label, _text in batch:
        label_list.append(float(_label))
        processed_text = torch.tensor(vocab(tokenizer(_text)))
        text_list.append(processed_text)
    return torch.tensor(label_list), pad_sequence(text_list, padding_value=1.0)


def main():
    """Main function to run the code."""
    # Load and preprocess the training data

    vectorizer = CountVectorizer()
    x_train = vectorizer.fit_transform(train_data['text'])
    y_train = train_data['label_text']

    # Encode labels
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)

    # Define dataset and dataloader
    train_dataset = CustomDataset(train_data['text'], y_train, vectorizer, y_train_encoded)
    train_loader = DataLoader(train_dataset, batch_size=3, shuffle=True)

    # Define model, loss function, and optimizer
    device = torch.device('cuda')
    input_size = x_train.shape[1]
    output_size = len(label_encoder.classes_)
    model = NeuralNetwork(input_size, output_size).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train the model
    num_epochs = 50
    for epoch in range(num_epochs):
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs.float())
            loss = criterion(outputs, targets.long())
            loss.backward()
            optimizer.step()

    # Load the test data
    test_data = pd.read_csv('./asg1_test.csv')
    x_test = vectorizer.transform(test_data['text'])

    # Make predictions
    model.eval()
    with torch.no_grad():
        inputs = torch.tensor(x_test.toarray(), dtype=torch.float32)
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        predictions = predicted.numpy()

    # Decode labels
    predicted_labels = label_encoder.inverse_transform(predictions)

    # Format Predictions and IDs for Submission
    submission_dict = {}
    for i, row in test_data.iterrows():
        ids = str(row['id']).split(',')
        for id_ in ids:
            submission_dict.setdefault(id_, []).append(predicted_labels[i])

    # Create a DataFrame from the submission dictionary
    submission_data = {'id': [], 'label_text': []}
    for id_, labels in submission_dict.items():
        submission_data['id'].append(id_)
        submission_data['label_text'].append(','.join(labels))

    submission_df = pd.DataFrame(submission_data)
    submission_df.to_csv('./asg1_submission.csv', index=False)

    # Define collate function for DataLoader

    # Define dataloader
    train_loader = DataLoader(train_data, batch_size=3, shuffle=False, collate_fn=collate_batch)
    test_loader = DataLoader(test_data, batch_size=3, shuffle=False, collate_fn=collate_batch)

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

    print(f'Test Loss: {test_loss / len(test_loader):.5f} | Test Acc: {test_acc / len(test_loader):.5f}%')


if __name__ == '__main__':
    main()
