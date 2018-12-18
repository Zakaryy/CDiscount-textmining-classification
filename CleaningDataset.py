def Cleaning(df, columns, html, lowercase, remove_caractere_spe, accent):
    '''
    This function allows the user to clean his dataset. It includes several arguments:
    - df : the user must specify the dataframe which need to be clean
    - columns : If the user wants to clean some columns of the specified's dtaframe, he must specify the name of the column. 
    If there are several columns, each variable must be separated by comma. For example, if we want to clean column A and B, 
    then the user has to specify [‘A’,’B’].
    - html : if the user wants to delete all the HTML tags then he must specify html = True.
    - lowercase : if the user wants to transform his sentences in lowercase then he must specify lowercase = True.
    - remove_caractere_spe : if the user wants to remove all special caracter like '?' or '!'
    then he must speciy remove_caractere_spe = True.
    - accent : if the user wants to remove all the accent then he must specify accent = True.
    '''
    import Librairies
    
    for i in columns:
        #chrono
        print("Start clean ", i)
        time_start = Librairies.time.time()

        #add blank space very usefull & mandatory
        df[i+'_clean'] = df[i].map( lambda x : ' ' + x + ' ' )
        
        if html:
            #Remove html stuff
            df[i+'_clean']= df[i+'_clean'].map(lambda x : Librairies.BeautifulSoup(x,"html.parser").get_text())
        else:
            df[i+'_clean'] = df[i+'_clean']
            
        if lowercase:
            #Put all words in lowcase
            df[i+'_clean'] = df[i+'_clean'].map(lambda x : x.lower())
        else:
            df[i+'_clean'] = df[i+'_clean']
            
        if remove_caractere_spe:
        #remove spe carac.
            df[i+'_clean'] = df[i+'_clean'].map(lambda x : x.replace(r"[^a-zA-Z0-9]", " "))
            df[i+'_clean'] = df[i+'_clean'].map(lambda x : x.replace("  ", " "))
        else:
            df[i+'_clean'] = df[i+'_clean']
            
        if accent:
            # remove accent
            df[i+'_clean'] = df[i+'_clean'].map(lambda x : Librairies.unicodedata.normalize('NFD', x).encode('ascii', 'ignore').decode('utf-8'))
        else:
            df[i+'_clean'] = df[i+'_clean']
        #chrono
        time_end = Librairies.time.time()
        print("Cleaning time: %d secondes"%(time_end-time_start))
    print("")    
    print('Shape of the df cleaned: ', df.shape)    
        
    return df