import numpy as np
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

d1 = pd.DataFrame({
    'name':['alice','bob','charlie','david','emily'],
    'class':['12b','11c','11a','12a','11b'],
    'state':['CG','Bihar','MP','Delhi','Assam']
})
print(d1)