import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
print(model.get_params())

grid = GridSearchCV(estimator=model,
                    param_grid={'criterion': ['gini', 'entropy'], 'splitter': ['best', 'random'], 'random_state': [x for x in range(5)]},
                    cv=4)

grid.fit(X_train, y_train)
df_grid = pd.DataFrame(grid.cv_results_)
#df_grid.to_csv('grid_results.csv')
#print(df_grid)
predictions = grid.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(accuracy)
