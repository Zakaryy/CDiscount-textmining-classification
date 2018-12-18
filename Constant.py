import Librairies
#REPERTORY 
REP_DATA_IN  = 'C:\\Users\\dylan\\PyBooks\\Cdiscount\\data\\'
DATABASE_LANGUAGE = 'french'
#REP_DATA_IN  = 'C:/Users/Compte Invité/TEAM_DZ/' 


#IMPORT

#Path of the csv file
I_FILE_IN      = REP_DATA_IN + "chanson.csv"
#Separator of the csv file
I_SEPARATOR	= '$'
#Encoding of the csv file
I_ENCODE = 'ansi'
#Useless columns 
I_COLS_TO_DROP = ['texte2','artiste_chanson','genre', 'genre2', 'count']


#SPLIT

#Proportion of the test base
S_PROPORTION = 0.3
#Seed of the split
S_SEED = 1434
#Target of the base (Y)
S_TARGET = 'Rap'
#Stratify the split
S_STRATIFY = True


#CLEANING

#Columns to clean
C_TEXT_COLS        = ['parole']
#Remove the html tag
C_HTML = True
#Tranform uppercase into lowercase
C_LOWERCASE = True
#remove special character (, ? ! etc.)
C_REMOVE_SPE_CHAR  = True
#remove all the accent
C_ACCENT = True


#NORMALIZATION


#Columns that will be normalized
N_COLUMNS_1 = 'parole_clean'
#Old cloumns
N_COLUMNS_OLD_1 = 'parole'
#Remove stopword in the selected columns
N_STOPWORDS_1 = True
#replace empty by underscore
N_UNDERSCORE_1 = False
#Delete a special char.
N_CHAR_TO_DELETE_1 = None
#count the number of words per lines
N_COUNTER_1 = False
#Join the word 'pour' with th word that follows it
N_POUR_1 = True
#Replace numbers into '(numbers)'
N_NUMBER_1 = '0'
#Apply stemming in the choosen language
N_ROOT_1 = 'root_stem'
#Apply a special treatment on the units of measurement 
N_UNITS_1 = False



#VECTORIZATION

#Columns to vectorize
V_NORMED_TEXT_COLS = ['parole_clean']
#Choose the weight of a colmun in the final base 
V_TEXT_COLS_WEIGHT = [1]
#Name of the merged columns
V_CONCAT_COL_NAME = 'concat_columns'
#TF-IDF Specifications
V_ANALYZ  = 'word'
V_BINARY = False
V_NORM = False
V_IDF = True
V_MINIMUM = 1
V_NGRAM = (1,1)


#ADD_FEATURE

#Add additional data to the matrix
#constantes pour le fichier optionnel pouvant contenir un ensemble de colonne numerique
#A_FILE_IN_VECTORS  = REP_DATA_IN + "X_fasttext_matrix_size500_window3_mincount1_iter20.csv"
A_FILE_IN_VECTORS  = '' #permet de savoir qu'il n'y en a pas
A_COLS_TO_DROP_VECTORS = ['Unnamed: 0', 'categorie1_id', 'new_id', 'categorie1_name']
A_ENCODE = "ansi"
A_SEPARATOR = ","
A_ID_ROW_VECTORS = 'id_pdt'
A_ID_ROW       = 'file'

#FEATURE_SELECTION
F_METHOD = 'chi2'
F_HYPERPARAMETER = 250

#MODELISATION
#Model Specifications
M_ESTIMATOR = Librairies.BernouilliNB()
M_PARAM = dict(alpha = Librairies.np.arange(0,1.1,0.1), fit_prior = [True, False])
M_CROSSVAL = 5
M_CORE = -1
M_STEP = 2
M_ITERATION = 10 
M_RANDOMIZED_SEARCH = True
M_NAME_OUTPUT = "Naive Bayesian - Rap - 250 features.txt"
M_NAME_ALGORITHM = "Naive Bayesian"