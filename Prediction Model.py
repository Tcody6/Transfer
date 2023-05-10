import numpy as np
import pandas as pd
import category_encoders as ce
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

players21 = pd.read_csv("players2021_output.csv")
players22 = pd.read_csv("players2021_output.csv")

players21['Rank'] = players21['Rank'].fillna(400)
players21['Height'] = players21['Height'].fillna(65.0)
players22['Rank'] = players22['Rank'].fillna(400)
players22['Height'] = players22['Height'].fillna(65.0)

players21 = players21[~pd.isnull(players21['transfer'])]
players22 = players22[~pd.isnull(players22['transfer'])]

all = pd.concat([players21, players22])

ce_OHE = ce.OneHotEncoder(cols=['class', 'Position'])
all = ce_OHE.fit_transform(all)

transfer = all['transfer']
all = all.drop(['transfer'], axis=1)

all['transfer'] = transfer

X_train, X_test, y_train, y_test = train_test_split(all.iloc[:,4:-1], all.iloc[:,-1], test_size= 0.3, shuffle=True)

boost = XGBClassifier(max_depth=10, n_estimators=1000,
    min_child_weight=0.5,
    colsample_bytree=0.8,
    subsample=0.8,
    eta=0.1,
    seed=42)

boost.fit(X_train, y_train)
boost_predict = boost.predict(X_test)

cm = confusion_matrix(y_test, boost_predict)

disp = ConfusionMatrixDisplay(cm)

disp.plot()
plt.show()

plt.bar(boost.feature_names_in_, boost.feature_importances_)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()