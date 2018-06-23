def normalization (df, columns, stopwords = '0', underscore = '0', char_to_delete = '0', counter = '0', pour = '0', nombre = '0', root = '0', units = '0'):
    #Add a separator "_" after the word "pour"
    #chrono
    print("Start Treatment  ", columns)
    time_start = time.time()
       
    if units == "units":
           
        #Thanks to this regex we distinguish the letter "l" and the unit of measurement "l" which refers to liter
        regex = re.compile(r'([a-z]) (l|m|s) ')
        df[columns] = df[columns].str.replace(r'([a-z]) (l|m|s) ', r'\1 ')
       
        dimension_regex = {
            k: '|'.join([r'(?<=[^a-zA-Z]){0}\s+'.format(t) for t in v])
            for k, v in dimensions.dimension.items()
        }
       
        for k, v in dimension_regex.items():
            df[k+'_'+columns] = 1*(df[columns].str.findall(v).str.len() > 0)
                      
    if pour == "pour":
        df[columns] = df[columns].map(lambda x : x.replace('pour ', 'pour_'))
    else:
        df[columns] = df[columns]
    #replace numbers by '(numbers) ' or delete numbers
    if nombre == 'numbers':
        df[columns] = df[columns].map(lambda x : re.sub(r'\s[0-9]+\s', ' (numbers) ', x))
    elif nombre == "no_numbers":
        df[columns] = df[columns].map(lambda x : re.sub('[^a-z_]', ' ', x))
    # remove french stop words + tokenisation
    #Put several files of stopwords ?
    if stopwords == "stopwords":
        df[columns] = df[columns].apply(lambda x: ' '.join([word for word in x.split() if word not in (lucene_stopwords)]))
    ### french stemming/Lemmatizing
    if root == 'root_stem':
        stemmer=nltk.stem.SnowballStemmer('french')
        df[columns] = df[columns].apply(lambda x : ' '.join([stemmer.stem(word) for word in x.split()]))
      #  tokens = [stemmer.stem(token) for token in tokens]
    else:
        lemmatizer = nltk.WordNetLemmatizer()
        df[columns] = df[columns].apply(lambda x : ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))
    #Encoding, extraction de variable
    #Create column : number of words
    if counter == "counter":
        df[columns+"_count"] = df[columns].map(lambda x : len(x.split(" ")))
    #replace empty by underscore
    if underscore == 'underscore':
        df[columns] = df[columns].map(lambda x : re.sub('[^a-zA-Z0-9]', '_', x).lower())
       
        #Replace the brand "AUCUNE" by space ?
 #   if aucune == 'aucune':
  #      df[columns] = df[columns].map(lambda x : x.replace('aucune',''))
        #Delete 'Voir la presention' or other char
    if char_to_delete is not None  :
        df[columns] = df[columns].map(lambda x : x.split(char_to_delete)[0])
    #chrono
    time_end = time.time()
    print("Treatment time: %d secondes"%(time_end-time_start))