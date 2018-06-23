def Cleaning(df, columns): #Add an argument "df" ? If we want to apply our function to our train or valid set.
    for i in columns:
                #chrono
        print("Start clean ", i)
        time_start = time.time()
   
        #Remove html stuff
        df[i+'_clean']= df[i].map(lambda x : BeautifulSoup(x,"html.parser",from_encoding='utf-8').get_text())
       
        #Put all words in lowcase
        df[i+'_clean'] = df[i+'_clean'].map(lambda x : x.lower())
       
        #remove spe carac.
        df[i+'_clean'] = df[i+'_clean'].map(lambda x : x.replace(r"[^a-zA-Z0-9]", " "))
        df[i+'_clean'] = df[i+'_clean'].map(lambda x : x.replace("  ", " "))
       
        #add blank space
        df[i+'_clean'] = df[i+'_clean'].map( lambda x : ' ' + x + ' ' )
        ### remove accent
        df[i+'_clean'] = df[i+'_clean'].map(lambda x : unicodedata.normalize('NFD', x).encode('ascii', 'ignore').decode("utf-8"))
       
        #chrono
        time_end = time.time()
        print("Cleaning time: %d secondes"%(time_end-time_start))