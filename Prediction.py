def prediction(search_method, X_test, Y_test, Y_train):
    
    import Librairies
    import Constant    
    
    y_pred = search_method.predict(X_test)
    print("Final Score:", Librairies.accuracy_score(Y_test, y_pred))