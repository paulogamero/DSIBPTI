#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paulogamero
"""
# ATIVIDADE: EXERCITANDO 3 - PARTE 02
# AUTOR: Paulo Gamero

import os
import pandas as pd
import nltk
from nltk.corpus import machado, stopwords

# 1) Execute print(machado.readme()) para conhecer melhor o corpus
print(machado.readme())

#LETRA A (Classifique as palavras de acordo com suas classes gramaticais de cada documento. Salve o corpus POS Tagged em uma planilha ou texto para uso posterior. É importante manter a informação sobre o documento origem dos novos documentos)
arq_casmurro = 'romance/marm08.txt'
arq_alienista= 'contos/macn003.txt'

casmurro = machado.words([arq_casmurro])
alienista = machado.words([arq_alienista])

stopword = stopwords.words('portuguese')
minha_stop_w = [',','[',':', '\'','.','...','?',']', '!','/','-',';','\x97','(',')','\x94.','\x93','\x92',]

casmurro_clear = [p for p in casmurro if (p not in stopword) and (p not in minha_stop_w)]
alienista_clear= [p for p in alienista if (p not in stopword) and (p not in minha_stop_w)][198:10232]

# Classes gramaticais (Tagged)
pos_tags_casmurro = nltk.pos_tag(casmurro_clear)
pos_tags_alienista= nltk.pos_tag(alienista_clear)

with open(os.getcwd()+'\Paulo_POS_Dom-Casmurro.txt', 'w',encoding='utf8') as txt:
    for p in pos_tags_casmurro:
        txt.write(str(p)+'\n')

with open(os.getcwd()+'\Paulo_POS_Alienista.txt', 'w',encoding='utf8') as txt:
    for p in pos_tags_alienista:
        txt.write(str(p)+'\n')

# LETRA B (Obtenha a lista de entidades em cada documento, salvando para uso posterior)
lista = [casmurro_clear, alienista_clear]
entidades_cas = []
rotulo_cas = []
entidades_ali = []
rotulo_ali = []
for x in lista:
    tokens = nltk.word_tokenize(' '.join(x))
    pos_tags = nltk.pos_tag(tokens)
    chuncks = nltk.ne_chunk(pos_tags, binary=True)
    for chunck in chuncks:
       if hasattr(chunck,'label'):
           if x == casmurro_clear:
               entidades_cas.append(' '.join(c[0] for c in chunck))
               rotulo_cas.append(chunck.label())
           else:
               entidades_ali.append(' '.join(c[0] for c in chunck))
               rotulo_ali.append(chunck.label())

entidades_casmurro_rotulos = list(set(zip(entidades_cas,rotulo_cas)))
entidades_alienista_rotulos= list(set(zip(entidades_ali,rotulo_ali)))

#LETRA C (Analisando os documentos marcados (tagged) tanto POS quanto NER, quais são as classes mais utilizadas?)
freq_casmurro = nltk.FreqDist(pos_tags_casmurro)
freq_alienista = nltk.FreqDist(pos_tags_alienista)

print(freq_casmurro.most_common(10))
print(freq_alienista.most_common(10))

# LETRA D (Observe que há uma tendência de que termos menos relevantes para a análise sejam mais frequentes. Então, repita os procedimentos anteriores, mas com os termos que são relevantes para uma análise do que está sendo falado (trata-se de uma análise preliminar e ainda superficial do discurso))
# RESPOSTA: O extração dos termos menos relevantes foi feita no início do processo, deixando apenas os termos relevantes.

# LETRA E (Determine o vocabulário comum entre os textos)
voc1 = set(casmurro_clear)
voc2 = set(alienista_clear)
vocabulario_comum = voc1 & voc2

# LETRA F (Determine a frequência de termos comuns nos dois textos, separadamente)
comum_casmurro = nltk.FreqDist(voc1)
comum_alienista= nltk.FreqDist(voc2)

# LETRA G (Determine a frequência de termos comuns utilizados pelo autor considerando os dois textos.)
comum = nltk.FreqDist(vocabulario_comum)

# LETRA H (Desafio: Quais são as entidades mais citadas pelo autor?)
print(f'Na obra Dom Casmurro as entidade mais citadas são: {nltk.FreqDist(entidades_cas).most_common(5)}')
print(f'Na obra O Alienista as entidade mais citadas são: {nltk.FreqDist(entidades_ali).most_common(5)}')