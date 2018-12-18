def tf_idf (df, columns, ponde, concat_columns_name, analyz, binar, norm, idf, minimum,Train,  ngram=(1,1)):
    import Librairies
    #Binar = True & norm = False & use_idf = False ==> TF Binaire
    #Binar = False & norm = False & use_idf = False ==> TF Frequency
    #Binar = False & norm = False & use_idf = True ==> TF IDF
    global matrix, vectorizer
    #chrono
    print("Start TF-IDF  ", concat_columns_name)
    time_start = Librairies.time.time()

    # create an empty column
    df[concat_columns_name] = ''

    for i, j in zip(columns, ponde):
        df[concat_columns_name] = df[concat_columns_name] + (' ' + j * (' ' + df[i]))
        df[concat_columns_name] = df[concat_columns_name].map(lambda x : x.lstrip(' '))
        

    if Train == True:
        
        vectorizer = Librairies.TfidfVectorizer(binary=binar, norm=norm, use_idf=idf, min_df=minimum, ngram_range=ngram, analyzer=analyz)

        matrix = vectorizer.fit_transform(df[concat_columns_name])
    else:
        matrix = vectorizer.transform(df[concat_columns_name])
        
    #chrono
    time_end = Librairies.time.time()
    print("TF-IDF time: %d secondes"%(time_end-time_start))
    print("")
    print("There is", list(matrix.shape)[1], "features")
        
    return matrix