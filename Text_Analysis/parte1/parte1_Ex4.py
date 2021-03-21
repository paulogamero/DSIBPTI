# ATIVIDADE: EXERCITANDO 4 - PARTE 01
# AUTOR: Paulo Gamero

from nltk.corpus import machado, stopwords
import nltk

# 1) Execute print(machado.readme()) para conhecer melhor o corpus
print(machado.readme())

# 2) Utilizando o corpus machado, elabore um programa que atenda aos requisitos:
# LETRA A
print(machado.categories())

# LETRA B
print(machado.fileids())

# LETRA C
arq = 'romance/marm05.txt'
words = machado.words([arq])
print(words)

# LETRA D
fdist = nltk.FreqDist(words)
for p in ['olhos','estado']:
     print(f'Arquivo {arq} e frequência da palavra {p} {fdist[p]}')

# LETRA E
print(f'Existem {len(words)} palavras no texto')

# LETRA F
print(f'São {len(fdist.keys())} palavras diferentes')

# LETRA G
print(f'O Vocabulário é {fdist.keys()}')

# LETRA H
print(f'Bigramas: {fdist.most_common(15)}')

# LETRA I
tab = fdist.tabulate(15)

# LETRA J
fdist.plot(15)

# LETRA K
stopword = stopwords.words('portuguese')
my_stop = [',','[',':', '\'','.','...','?',']', '!','/','-',';','\x97','(',')','\x94.','\x93','\x92',]

clear = [p for p in words if (p not in stopword) and (p not in my_stop)]
clear_n=nltk.FreqDist(clear)
print(f'Os 15 termos mais comuns após o stopwords são: {clear_n.most_common(15)}')
clear_n.plot(15)

# LETRA L
tri = [n for n in nltk.ngrams(clear,3)]
tri_n= nltk.FreqDist(tri)

# LETRA M

bi = [p for p in nltk.ngrams(clear,2) if 'olhos' in p ]
bi_olhos = nltk.FreqDist(bi).most_common(15)

# LETRA N
nltk.FreqDist(bi).plot(15)