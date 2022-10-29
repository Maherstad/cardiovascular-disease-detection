def preprocessing_p1(df):
    #drop id due to high cardinality
    df=df.drop('id', axis=1)
    
    df['age']=df['age']/365
    
    #ap_hi maximum value 190
    #ap_hi minimum value 100
    def mod_ap_hi(entry):
        if entry>190:
            return 190
        elif entry<100:
            return df['ap_hi'].median()
        else:
            return entry
    
    df['ap_hi']=df['ap_hi'].apply(mod_ap_hi)
    
    #ap_lo maximum value 70 
    #ap_lo minimum value 40 
    def mod_ap_lo(entry):
        if entry>70:
            return 70
        elif entry<40:
            return df['ap_lo'].median()
        else:
            return entry
        
    df['ap_lo']=df['ap_lo'].apply(mod_ap_lo)
    
    return df 