def split_dataset (data_input, x, seed, var_y, ID):
    '''
    The split_dataset funtion allows the user to plit its dataframe into 3 dataframe (TEST, Train_X and Train_Y)
    This funciton includes several arguments :
data_input : name of the dataframe that you want to split.
    x : determine the proprtion of the test size split.
    seed : seed of the random split
    var_y : insert here the variable to explain.
    ID : name of the ID column
    '''
   
    #use the variable outside of the function
    global data_train_x , data_train_y
    nb_rows_input = list(data_input.shape)[0]
   
        #chrono
    print("Start split %d lines" %nb_rows_input)
    time_start = time.time()
   
    #separer la Dataframe en 2, data_train and data_valid
    data_train, data_test = train_test_split(data_input, test_size = x, random_state = seed)
       
    #chrono
    time_end = time.time()
    print("Split time: %d secondes"%(time_end-time_start))
   
    print('data_input :', data_input.shape)
    print('data_train :', data_train.shape)
    print('data_train :', data_test.shape)
    data_train_y = data_train[[ID,var_y]]
    data_train_x = data_train.drop([var_y], axis=1)
    print('data_train_x :', data_train_x.shape)
    print('data_train_y :', data_train_y.shape)

