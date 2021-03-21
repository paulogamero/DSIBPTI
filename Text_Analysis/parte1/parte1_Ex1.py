#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:43:52 2021

@author: paulogamero
"""
# ATIVIDADE: EXERCITANDO 1 - PARTE 01
# AUTOR: Paulo Gamero

from nltk.corpus import CategorizedPlaintextCorpusReader

d = CategorizedPlaintextCorpusReader(
    r'C:\Users\Usuario\Dropbox\Pos\Pós DataScience\4 - Análise de textos com R e Python\Dados\mix20_rand700_tokens_cleaned\tokens',
r'.*.txt', cat_pattern = r'(\w+)/*', encoding = 'iso8859-1')

for p in d.words('pos/cv003_tok-8338.txt'):
    print(p + ' ', end = '')

for n in d.words('neg/cv002_tok-3321.txt'):
    print(n + ' ', end = '')