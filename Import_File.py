#attention la premiere ligne du csv devra contenir les nom des colonnes

#Columns names if rename needed
#HEADER_TRAIN =['Identifiant_produit','Categorie1','Categorie2','Categorie3','Description','Libelle','Marque','Produit_Cd','Prix']


def csv_to_df(path_filename, separator, encode, drop_no_columns=None):
    '''
    The csv_to_df funtion allows the user to import its csv file into a dataframe
    This funciton includes several arguments :  
    - path_filename : the user has to specify the path/file_name in which their csv file is.
    - separator : if their csv file contain a specific separator, the user can specify it here
    - encode : if the database contains some special characters, the user can specify the encoding UTF-8 or ANSI.
    - drop_no_columns : If the user wants to drop some useless columns, he must specify the name of the column. 
    If there are several columns, each variable must be separated by comma. For example, if we want to drop column A and B, 
    then the user has to specify [‘A’,’B’].
    On the other hand, if there is none columns to drop then the user as to specify an empty bracket like [].
    '''    
    #use the variable outside of the function
    #import time
    #import pandas as pd
    import Librairies

    #chrono
    print("Start import")
    time_start = Librairies.time.time()
    
    #csv to df
    data_all = Librairies.pd.read_csv(path_filename,sep=separator, encoding=encode, header= 0)
    data_all = data_all.fillna("")
    
    #delete columns
    if drop_no_columns != None:
        data_all.drop(drop_no_columns, axis = 1, inplace=True)

    #chrono
    time_end = Librairies.time.time()

    print("Import time: %d secondes"%(time_end-time_start))
    print('Shape :', data_all.shape)
    
    return data_all