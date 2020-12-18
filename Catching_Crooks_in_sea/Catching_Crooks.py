import sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


import pickle 

"""Python pickle module is used for serializing and de-serializing a Python object structure. 
Any object in Python can be pickled so that it can be saved on disk. 
What pickle does is that it “serializes” the object first before writing it to file. 
Pickling is a way to convert a python object (list, dict, etc.) into a character stream. 
The idea is that this character stream contains all the information necessary to reconstruct the object in another python script."""


# Model Building and training
df = pd.read_csv('fishing_vessels_v1.csv')

x, y = df.loc[:, 'active_2012':'active_2015'], df.loc[:, 'active_2016']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10, test_size=0.3, shuffle=True)


# Using Decision Tree Algorithm
dt = DecisionTreeClassifier()

dt.fit(x_train, y_train)


pickle.dump(dt, open('catching_crooks.pkl','wb')) 

# We are dumping the model into catching_crooks.pkl file so that there is no need to run Catching_Crooks.py file everytime


model = pickle.load(open('catching_crooks.pkl', 'rb'))
