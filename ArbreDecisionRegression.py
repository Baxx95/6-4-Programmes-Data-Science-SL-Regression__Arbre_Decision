import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeRegressor

#from sklearn import tree
#from sklearn.externals.six import StringIO 
#from IPython.display import Image 
#from sklearn.tree import export_graphviz
#import pydotplus
#import os


df = pd.read_csv('prediction_de_fraud.csv')


target = df['amount'].values


X = df[['step','type','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','isFraud','isFlaggedFraud']].values




#Données catégoriques
labEncr_X = LabelEncoder()
X[:,1] = labEncr_X.fit_transform(X[:,1])

# scindons les données en d'entrainement et ensembles de test

X_train, X_test, y_train, y_test = train_test_split(X, target, test_size = 0.3, random_state = 42)

#Ensuite, nous construisons le régresseur d' arbre de décisionen utilisant la DecisionTreeRegressor()fonction.
dt_reg = DecisionTreeRegressor(max_depth = 10, min_samples_leaf = 0.2, random_state= 50)
"""
dt_reg.fit(X_train, y_train)
y_pred=dt_reg.predict(X_test)



ind_var = df[['step','type','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','isFraud','isFlaggedFraud']]

data = tree.export_graphviz(dt_reg, out_file=None, feature_names= ind_var.columns.values, proportion= True)


graph = pydotplus.graph_from_dot_data(data) 

# observer graph
Image(graph.create_png())
