import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df=pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/healthcare_dataset.csv")
x = df[[ 'Age', 'Gender', 'Blood Type', 'Medical Condition', 'Insurance Provider','Billing Amount', 'Room Number', 'Admission Type','Medication']]
y = df['Test Results']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=21)

#Data pre-processing
label_encoder = LabelEncoder()

# features = ['Gender']
# for feature in features:
#     df[feature] = pd.serlabel_encoder.fit_transform(df[feature])
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df['Blood Type'] = label_encoder.fit_transform(df['Blood Type'])
df['Medical Condition'] = label_encoder.fit_transform(df['Medical Condition'])
df['Insurance Provider'] = label_encoder.fit_transform(df['Insurance Provider'])
df['Admission Type'] = label_encoder.fit_transform(df['Admission Type'])
df['Medication'] = label_encoder.fit_transform(df['Medication'])
df['Test Results'] = label_encoder.fit_transform(df['Test Results'])

#Model
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(y_test)


accuracy = accuracy_score(y_test, y_pred)
print("accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()