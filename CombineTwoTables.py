import pandas as pd

a1 = {'personID':[1,2],'lastname':['Wang','Alice'],'firstname':['Allen','Bob']}
pTable = pd.DataFrame(data=a1)

a2 = {'addressID':[1,2],'personID':[2,3],'city':['New York City','Leetcode'],'state':['New York','California']}
aTable = pd.DataFrame(data=a2)

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame):
    df = pd.DataFrame({})
    df = df.append(person)
    max_pID = df['personID'].max()
    
    i=0
    ii=0
    for i in range(0,max_pID):
        for ii in range(0,)
        if df.loc[i,'personID'] == address.loc{}
        
        
        Some changes
        

    
    
     