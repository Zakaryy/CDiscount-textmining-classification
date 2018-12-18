def split_dataset (data_input, proportion, seed, var_y, strat):
    '''
    The split_dataset funtion allows the user to plit its dataframe into 3 dataframe (TEST, Train_X and Train_Y)
    This funciton includes several arguments :

    data_input : name of the dataframe that you want to split.
    proportion : determine the proprtion of the test size split.
    seed : seed of the random split
    var_y : insert here the variable to explain.
    '''
    
    #use the variable outside of the function
    import Librairies
    #from sklearn.model_selection import train_test_split    
    
    global data_train_x , data_train_y, data_test_x, data_test_y, data_train, data_test

    nb_rows_input = list(data_input.shape)[0]
    
        #chrono
    print("Start split %d lines" %nb_rows_input)
    time_start = Librairies.time.time()
    
    #separer la Dataframe en 2, data_train and data_valid
    if strat == True:
        data_train, data_test = Librairies.train_test_split(data_input, test_size = proportion, random_state = seed, stratify = data_input[var_y])
    else:
        data_train, data_test = Librairies.train_test_split(data_input, test_size = proportion, random_state = seed)        
    #chrono
    time_end = Librairies.time.time()
    print("Split time: %d secondes"%(time_end-time_start))
    
    print('Shape of the database:', data_input.shape)
    print('Shape of the data_train :', data_train.shape)
    print('Shape of the data_test :', data_test.shape)

    data_train_y = data_train[var_y]
    data_test_y = data_test[var_y]
    data_test_x = data_test.drop([var_y], axis = 1)
    data_train_x = data_train.drop([var_y], axis=1)
    df_pred = data_train_x.copy()

    print('Shape of the TRAIN_X: ', data_train_x.shape)
    print('Shape of the TRAIN_Y: ', data_train_y.shape)
    print('Shape of the TEST_X: ', data_test_x.shape)
    print('Shape of the TEST_Y: ', data_test_y.shape)
    print('Shape of the data_pred: ', data_train_x.shape)
    
    return data_train_x, data_train_y, data_test_x, data_test_y, df_pred    