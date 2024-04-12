import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import DataLoader, Dataset


# Define a simple neural network classifier
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        x = torch.sigmoid(self.fc(x))
        return x


# Custom dataset class to load and preprocess data
class CustomDataset(Dataset):
    def __init__(self, texts, labels, vectorizer):
        self.texts = texts
        self.labels = labels
        self.vectorizer = vectorizer

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        text_vec = self.vectorizer.transform([text]).toarray().squeeze()
        return text_vec, label


# Load and preprocess the training data
train_data = pd.read_csv('./asg1_train.csv')
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['text'])
y_train = train_data['label_text']

# Encode labels
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)

# Define dataset and dataloader
train_dataset = CustomDataset(train_data['text'], y_train_encoded, vectorizer)
train_loader = DataLoader(train_dataset, batch_size=3, shuffle=True)

# Define model, loss function, and optimizer
input_size = X_train.shape[1]
output_size = len(label_encoder.classes_)
model = NeuralNetwork(input_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
num_epochs = 50
for epoch in range(num_epochs):
    for inputs, targets in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs.float())
        loss = criterion(outputs, targets.long())  # targets converted to Long type
        loss.backward()
        optimizer.step()

# Load the test data
test_data = pd.read_csv('./asg1_test.csv')
X_test = vectorizer.transform(test_data['text'])

# Make predictions
model.eval()
with torch.no_grad():
    inputs = torch.tensor(X_test.toarray(), dtype=torch.float32)
    outputs = model(inputs)
    _, predicted = torch.max(outputs, 1)
    predictions = predicted.numpy()

# Decode labels
predicted_labels = label_encoder.inverse_transform(predictions)

# Format Predictions and IDs for Submission
submission_dict = {}
for i, row in test_data.iterrows():
    ids = str(row['id']).split(',')  # Split the IDs if there are multiple IDs
    for id_ in ids:
        submission_dict.setdefault(id_, []).append(predicted_labels[i])

# Create a DataFrame from the submission dictionary
submission_data = {'id': [], 'label_text': []}
for id_, labels in submission_dict.items():
    submission_data['id'].append(id_)
    submission_data['label_text'].append(','.join(labels))

submission_df = pd.DataFrame(submission_data)

# Save Predictions to CSV
submission_df.to_csv('./asg1_submission.csv', index=False)
print('Done.')
