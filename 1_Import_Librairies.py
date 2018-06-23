import unicodedata
import time #chrono to test perform of the cleaning
import pandas as pd #dataframe library
import numpy as np #statistic library
import random
import nltk #Natural Language Toolkit
import collections #add-on datatypes treatments
import dimensions #import a dimension file (dict)
import itertools #iterator
import csv
import warnings
from bs4 import BeautifulSoup #Nettoyage d'HTML
import re # Regex
import nltk # Nettoyage des données
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

lucene_path = input('Input path of lucene_stopwords file: ')

lucene_stopwords = open(lucene_path+"lucene_stopwords.txt","r").read().split(",")
