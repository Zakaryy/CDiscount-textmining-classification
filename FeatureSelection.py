def FeatureSelection(X, Y, method, HyperParameter):
    import Librairies
    global features
    if method.upper() == 'LASSO':
        lsvc = Librairies.LinearSVC(C=HyperParameter, penalty="l1", dual=False).fit(X, Y)
        print("HyperParameter of Lasso Regression is C: ", HyperParameter)
        model = Librairies.SelectFromModel(lsvc, prefit=True)
        features = model.transform(X)
    elif method.upper() == 'RNF':
        clf = Librairies.ExtraTreesClassifier(max_depth = HyperParameter, random_state=0, n_jobs=-1)
        clf = clf.fit(X, Y)
        print("HyperParameter of Random Forest is Max_depth: ", HyperParameter)
        model = Librairies.SelectFromModel(clf, prefit=True)
        features = model.transform(X)
    elif method.upper() == 'CHI2':
        features = Librairies.SelectKBest(Librairies.chi2, HyperParameter).fit_transform(X, Y)
        print("HyperParameter of Chi Square is the number of features: ", HyperParameter)
    print("")
    print("Numbers of features selected thanks to the HyperParameter: ", list(features.shape)[1])
    return features