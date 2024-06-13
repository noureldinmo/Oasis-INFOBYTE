# Email Spam Detection using Logistic Regression
This project implements an email spam detection model using Logistic Regression. The dataset used for this project is the "spam.csv" file which contains labeled email data for training and testing the model.

## Project Structure
spam.csv: Dataset containing email texts and labels (spam/ham).
spam_detection.py: Python script to load data, preprocess, train, evaluate the model, and run test cases.
README.md: Project description and instructions.

### Requirements
Python 3.x
Pandas
Scikit-learn

#### You can install the required Python packages using:
pip install pandas scikit-learn

### Dataset
The dataset spam.csv should contain the following columns:
v1: Label (spam/ham)
v2: Email text

#### Script Overview
The main script spam_detection.py performs the following steps:

#### Load and Preprocess the Data:

Load the dataset with appropriate encoding handling.
Rename columns for convenience.
Drop any rows with missing values.
Encode labels (spam: 1, ham: 0).

#### Feature Extraction:
Transform the email texts into TF-IDF features.

##### Train-Test Split:
Split the data into training and testing sets.

#### Train the Model:
Train a Logistic Regression model on the training data.

#### Evaluate the Model:
Evaluate the model's performance on the test set using accuracy and classification report.

#### Run Test Cases:
Predict and display labels for a set of sample test texts.

##### Usage
To run the script, execute the following command in your terminal:
python spam_detection.py

###### Sample Test Cases
The script includes a few test cases to demonstrate the model's predictions:

"Congratulations! You've won a free ticket to the Bahamas. Call now!"
"Hi John, are we still on for the meeting tomorrow?"
"Get your free coupon now by clicking here!"
"It was great catching up with you last week. Let's do it again sometime."
"Urgent! Your account has been compromised. Please verify your identity."
These sample texts will be classified as either "spam" or "ham" by the trained model.

###### Example Output
After running the script, you should see an output similar to:

plaintext
Copy code
Test Accuracy: 0.9800
Classification Report:
              precision    recall  f1-score   support

         ham       0.98      1.00      0.99       965
        spam       1.00      0.95      0.97       150

    accuracy                           0.98      1115
   macro avg       0.99      0.97      0.98      1115
weighted avg       0.98      0.98      0.98      1115

Text: Congratulations! You've won a free ticket to the Bahamas. Call now!
Predicted Label: spam

Text: Hi John, are we still on for the meeting tomorrow?
Predicted Label: ham

Text: Get your free coupon now by clicking here!
Predicted Label: spam

Text: It was great catching up with you last week. Let's do it again sometime.
Predicted Label: ham

Text: Urgent! Your account has been compromised. Please verify your identity.
Predicted Label: spam
