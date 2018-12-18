def AddFeature(df, vect_matrix):
    import Librairies
    import Import_File
    import Constant
    
    
    if Constant.A_FILE_IN_VECTORS != '':
        imp = Import_File.csv_to_df(Constant.A_FILE_IN_VECTORS, Constant.A_SEPARATOR, Constant.A_ENCODE, Constant.A_COLS_TO_DROP_VECTORS )
        df = Librairies.pd.merge(df, imp, how='left', left_on=Constant.A_ID_ROW, right_on = Constant.A_ID_ROW_VECTORS)
        df.drop([Constant.A_ID_ROW, Constant.V_CONCAT_COL_NAME] + Constant.V_NORMED_TEXT_COLS + [Constant.A_ID_ROW_VECTORS], axis=1, inplace=True)
        dense_matrix_1 = Librairies.np.array(df.as_matrix(columns = None), dtype=bool).astype(Librairies.np.int)
        sparse_matrix_1 = Librairies.csr_matrix(dense_matrix_1)
        print("Numbers of features added:", list(sparse_matrix_1.shape)[1])
        print("Then, there is in total", list(sparse_matrix_1.shape)[1] + list(vect_matrix.shape)[1], "features")

    elif Constant.A_FILE_IN_VECTORS == '':
        df.drop([Constant.A_ID_ROW, Constant.V_CONCAT_COL_NAME] + Constant.V_NORMED_TEXT_COLS, axis=1, inplace=True)
        dense_matrix_1 = Librairies.np.array(df.as_matrix(columns = None), dtype=bool).astype(Librairies.np.int)
        sparse_matrix_1 = Librairies.csr_matrix(dense_matrix_1)
        print("Numbers of features added:", list(sparse_matrix_1.shape)[1])
        print("Then, there is in total", list(sparse_matrix_1.shape)[1] + list(vect_matrix.shape)[1], "features")

    return Librairies.hstack((sparse_matrix_1, vect_matrix))
