import nltk
from nltk.corpus import jeita
from nltk.corpus import knbc

jfull_t = nltk.Text(jeita.words())           # create NLTK Text from JEITA Corpus
kfull_t = nltk.Text(knbc.words())            # create NLTK Text from KNB Corpus

fdist_jfull = nltk.FreqDist(jfull_t)         # create frequency dist from JEITA Corpus
print(fdist_jfull.most_common(50))           # 50 most common words in JEITA Corpus
fdist_kfull = nltk.FreqDist(kfull_t)         # create frequency dist from KNB Corpus
print(fdist_kfull.most_common(50))           # 50 most common words in KNB Corpus



# words that appear in the same context (same words on either side) as '人'
print(jfull_t.similar("人"))
print(kfull_t.similar("人"))