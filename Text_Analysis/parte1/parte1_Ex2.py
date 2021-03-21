# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:27:37 2021

@author: paulo
"""
# ATIVIDADE: EXERCITANDO 2 - PARTE 01
# AUTOR: Paulo Gamero

import docx
import nltk
from nltk import ngrams

arq = docx.Document('C:\\Users\\Usuario\\Dropbox\\Pos\\Pós DataScience\\4 - Análise de textos com R e Python\\Dados\\Noticia_1.docx')

txt_comp = []
for p in arq.paragraphs:
    txt_comp.append(p.text)
string = '\n'.join(txt_comp)

bigrama = []
for ng in ngrams(string.split(),2):
    bigrama.append(ng)

freq = nltk.FreqDist(bigrama)
print(freq.most_common(20))

trigrama = []
for ng in ngrams(string.split(),3):
    trigrama.append(ng)

freq_t = nltk.FreqDist(trigrama)
print(freq_t.most_common(20))