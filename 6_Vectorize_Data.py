def tf_idf (df, columns, ponde, concat_columns_name , analyz , binar,  ngram):
   
    global matrix , df_matrix , res , data_train_x
    #chrono
    print("Start TF-IDF  ", concat_columns_name)
    time_start = time.time()
    # create an empty column
    df[concat_columns_name] = ''
    for i, j in zip(columns, ponde):
        df[concat_columns_name] = df[concat_columns_name] + (j * df[i])
   
    vectorizer = CountVectorizer(analyzer=analyz, binary=binar,  ngram_range=ngram)
    
    matrix = vectorizer.fit_transform(df[concat_columns_name])
   
      
    df_matrix = pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names())
    n = df_matrix.shape
    print('matrix dimensions :', n)
    print('Number of columns :', list(df_matrix.shape)[1])
   
    #res = pd.concat([df, df_matrix], axis=1)
   
    #chrono
    time_end = time.time()
    print("TF-IDF time: %d secondes"%(time_end-time_start))