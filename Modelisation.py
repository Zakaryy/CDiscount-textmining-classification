def SearchCV(X, Y, estimator, param, crossval, nb_coeur, etape, random_search = False, iteration = None):
    import Librairies
    import Constant

    global search
    param_dist = param
    #NAME_ALGO = Constant.NAME_ALGORITHM
    #RANDOM_SEARCH = Constant.RANDOMIZED_SEARCH
    
    if random_search:
        search = Librairies.RandomizedSearchCV(estimator, param_distributions=param_dist, cv = crossval,
                                       n_iter=iteration, n_jobs = nb_coeur, verbose = etape)
    else:
        search = Librairies.GridSearchCV(estimator, param_distributions=param_dist, cv = crossval,
                                       n_jobs = nb_coeur, verbose = etape)
        
    start = Librairies.time.time()
    search.fit(X, Y)
    
    with open(Constant.REP_DATA_IN + Constant.M_NAME_OUTPUT, 'a', encoding='utf-8') as f:
        for i in range(1, 4):
            candidates = Librairies.np.flatnonzero(search.cv_results_['rank_test_score'] == i)
            for candidate in candidates:
                f.write("Algorithm: %s \r\n" % Constant.M_NAME_ALGORITHM)
                f.write("Model with rank: %d \r\n" % i)
                f.write("Mean validation score: %f (std: %f) \r\n" % (search.cv_results_['mean_test_score'][candidate],search.cv_results_['std_test_score'][candidate]))
                f.write("Parameters: %s \r\n" % search.cv_results_['params'][candidate])
                f.write("\r\n")
    f.close()
    
    return search    