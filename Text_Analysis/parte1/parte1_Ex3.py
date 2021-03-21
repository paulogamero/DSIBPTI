# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:14:54 2021

@author: paulo
"""
# ATIVIDADE: EXERCITANDO 3 - PARTE 01
# AUTOR: Paulo Gamero

#Analise a frequência das palavras [‘the’,’that’] no arquivo singles.txt e,depois, no arquivo pirates.txt.
from nltk.corpus import webtext, stopwords
from nltk import  ngrams
from nltk import tokenize
import nltk
import matplotlib.pyplot as plt

single = webtext.words('singles.txt')
pirate = webtext.words('pirates.txt')
stopword = stopwords.words('english')
minha_stop_w = [',','[',':', '\'','.','...','?',']', '!','/','-',';','\x97','(',')','\x94.','\x93','\x92',]

def token(palavras):
    stopwords_pt = stopwords.words('english')
    my_stop = [',','.','[',']','...',':','\'','?','!','/']
    return [x for x in palavras if (x is not stopwords_pt) and (x is not my_stop)]

# INCLUA A GERAÇÃO DE UM GRÁFICO DE FREQUENCIA
def freq(arquivo):
    palavras = webtext.words(arquivo)
    that = nltk.FreqDist([s for s in token(palavras) if s == 'that'])
    #that.plot(cumulative = True)
    the = nltk.FreqDist([s for s in token(palavras) if s == 'the'])
    #the.plot(cumulative = True)
    return print(f'O arquivo {arquivo} possui {that["that"]} "that" e {the["the"]} "the".')

freq('singles.txt')
clear = [c for c in single if (c not in stopword) and (c not in minha_stop_w)]

bi = [b for b in nltk.ngrams(clear,2)]
bi_n= nltk.FreqDist(bi).most_common(15)

quad = [ q for q in nltk.ngrams(clear,4) if 'life' in q ]
quad_n= nltk.FreqDist(quad).most_common(20)
print(quad_n)