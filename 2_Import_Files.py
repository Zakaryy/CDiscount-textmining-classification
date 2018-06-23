#attention la premiere ligne du csv devra contenir les nom des colonnes
#Columns names if rename needed
#HEADER_TRAIN =['Identifiant_produit','Categorie1','Categorie2','Categorie3','Description','Libelle','Marque','Produit_Cd','Prix']

def csv_to_df(path, file_name, separator, nb_rows, encode, drop_no_columns):
    '''
    The csv_to_df funtion allows the user to import its csv file into a dataframe
    This funciton includes several arguments :
    path : the user has to specify the path in which their file is.
    file_name : the name of their csv file (the real name)
    separator : if their csv file contain a specific separator, the user can specify it here
    nb_rows : The user must specify how many rows do their file contain
    encode : if the database contains some special characters, the user can specify the encoding UTF-8 or ANSI.
    drop_no_columns : if the user wants to drop some useless columns
    '''
   
    #use the variable outside of the function
    global data_all, DATA_DIR
   
    #chrono
    print("Start import %d lines" %nb_rows)
    time_start = time.time()
   
    #file path
    DATA_DIR = path
    df = DATA_DIR + file_name
   
    #csv to df
    data_all1 = pd.read_csv(df,sep=separator,nrows=nb_rows, encoding=encode, header= 0)
    data_all1 = data_all1.fillna("")
   
    #delete price and produit_Cd colums
    data_all1.drop(data_all1.columns[drop_no_columns], axis=1, inplace=True)
   
    #copying dataframe
      
    data_all=data_all1.copy()
   
    #chrono
    time_end = time.time()
    print("Import time: %d secondes"%(time_end-time_start))
   
    print('Shape :', data_all.shape)

    