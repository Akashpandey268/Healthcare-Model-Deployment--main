

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE


def prediction(new_data):

 data=pd.read_csv('health care diabetes.csv')

 x=data.drop([['Outcome','BloodPressure','SkinThickness']],axis=1)
 y=data['Outcome']
 trainx,testx,trainy,testy =train_test_split(x,y,test_size=0.20,random_state=44)
 sm = SMOTE(random_state =63)
 trainx_res,trainy_res = sm.fit_resample(trainx,trainy.ravel())  
 rf_grid=RandomForestClassifier(criterion= 'gini',max_depth=2,max_leaf_nodes=2,max_samples=3,min_samples_leaf= 1,
                               min_samples_split=3,n_estimators=400,random_state=46)
 rf_grid.fit(trainx_res,trainy_res)

 return rf_grid.predict(testx[0])