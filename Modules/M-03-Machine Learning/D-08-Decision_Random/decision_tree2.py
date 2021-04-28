import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


# with open('zoo.data') as my_file:
#     data = my_file.read()
zoo_df = pd.read_csv('zoo.data', header=None)
#print(zoo_df.shape)
#print(zoo_df.head())
#print(zoo_df.head())
#zoo_df = pd.DataFrame(data[0], index=None)
X = zoo_df.iloc[:, 1:17]
#print(X)
y = zoo_df[17]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# model = DecisionTreeClassifier(random_state=6)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(predictions)
# print(y_test.values)
#
# accuracy = accuracy_score(y_test, predictions)
# print(accuracy)
# matrix = confusion_matrix(y_test,predictions)
# print(matrix)

model = RandomForestClassifier(min_samples_split=2)


model.fit(X_train, y_train)

predictions2 = model.predict(X_test)

print(predictions2)
print(y_test.values)

accuracy = accuracy_score(y_test, predictions2)
print(accuracy)
matrix2 = confusion_matrix(y_test, predictions2)
print(matrix2)
