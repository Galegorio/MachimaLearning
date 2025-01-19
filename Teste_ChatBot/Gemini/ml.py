import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import google.generativeai as gemini

def ml():
    try:
        ar = pd.read_csv("dados.csv")
        vetor = TfidfVectorizer()
        pergunta = ar.pergunta

        x = vetor.fit_transform(pergunta)
        y = ar.funcao

        x_treino,x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.15, random_state=33)

        modelo = MultinomialNB();
        modelo.fit(x_treino,y_treino)
        print("Treino feito com sucesso!")
    except:
        print("Error")
