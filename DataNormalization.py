#Attention Constant.DATABASE_LANGUAGE

def normalization (df, columns, columns_old, stopwords = False, underscore = False, 
                   char_to_delete = None, counter = False, pour = False, nombre = '0', root = 'root_stem', units = False):

    import Librairies
    import Constant

    global langue
    
    langue = Constant.DATABASE_LANGUAGE
    
    #chrono
    print("Start Treatment  ", columns)
    time_start = Librairies.time.time()
    
    if char_to_delete is not None  :
        df[columns] = df[columns].map(lambda x : x.split(char_to_delete)[0])
    else:
        df[columns] = df[columns]
        
    if units:
            
        #Thanks to this regex we distinguish the letter "l" and the unit of measurement "l" which refers to liter
        #regex = re.compile(r'([a-z]) (l|m|s) ')
        df[columns] = df[columns].str.replace(r'([a-z]) (l|m|s) ', r'\1 ')
        
        dimension_regex = {
            k: '|'.join([r'(?<=[^a-zA-Z]){0}\s+'.format(t) for t in v])
            for k, v in Librairies.dimensions.dimension.items()
        }
        
        for k, v in dimension_regex.items():
            df[k+'_'+columns] = 1*(df[columns].str.findall(v).str.len() > 0)
                       

    if pour:
        df[columns] = df[columns].map(lambda x : x.replace('pour ', 'pour_'))
    else:
        df[columns] = df[columns]
    #replace numbers by '(numbers) ' or delete numbers
    if nombre == 'numbers':
        df[columns] = df[columns].map(lambda x : Librairies.re.sub(r'[0-9]+', ' (numbers) ', x)) #r'\s[0-9]+\s'
    elif nombre == "no_numbers":
        df[columns] = df[columns].map(lambda x : Librairies.re.sub('[^a-z_]', ' ', x))

    # remove french stop words + tokenisation
    #Put several files of stopwords ?
    if stopwords:
        df[columns] = df[columns].apply(lambda x: ' '.join([word for word in x.split() if word not in (Librairies.lucene_stopwords.lucene)]))
    ### french stemming/Lemmatizing
    if root == 'root_stem':
        stemmer=Librairies.nltk.stem.SnowballStemmer(Constant.DATABASE_LANGUAGE)
        df[columns] = df[columns].apply(lambda x : ' '.join([stemmer.stem(word) for word in x.split()]))
      #  tokens = [stemmer.stem(token) for token in tokens]
    elif root == 'root_lem':
        lemmatizer = Librairies.nltk.stem.WordNetLemmatizer(Constant.DATABASE_LANGUAGE)
        df[columns] = df[columns].apply(lambda x : ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))
    else:
        df[columns] = df[columns]
    #Encoding, extraction de variable
    #Create column : number of words
    if counter:
        df[columns+"_count"] = df[columns].map(lambda x : len(x.split(" ")))
    #replace empty by underscore
    if underscore:
        df[columns] = df[columns].map(lambda x : Librairies.re.sub('[^a-zA-Z0-9]', '_', x).lower())
        
    df.drop([columns_old], axis = 1, inplace=True)

    #chrono
    time_end = Librairies.time.time()
    print("Treatment time: %d secondes"%(time_end-time_start))
    print("")
    print("Shape of the dataset normalized:", df.shape)
    
    return df
