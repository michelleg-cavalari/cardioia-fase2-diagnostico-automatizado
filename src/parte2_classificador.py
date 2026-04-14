import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO_DADOS = os.path.join(BASE_DIR, "data", "frases_risco.csv")

def main():
    df = pd.read_csv(ARQUIVO_DADOS)

    print("=" * 60)
    print("CARDIOIA - CLASSIFICADOR DE RISCO")
    print("=" * 60)
    print("\nBase de dados:")
    print(df.head())

    X = df["frase"]
    y = df["situacao"]

    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer()
    X_treino_tfidf = vectorizer.fit_transform(X_treino)
    X_teste_tfidf = vectorizer.transform(X_teste)

    modelo = LogisticRegression()
    modelo.fit(X_treino_tfidf, y_treino)

    previsoes = modelo.predict(X_teste_tfidf)

    acuracia = accuracy_score(y_teste, previsoes)

    print("\nAcurácia:", round(acuracia, 2))
    print("\nRelatório de classificação:")
    print(classification_report(y_teste, previsoes))
    print("Matriz de confusão:")
    print(confusion_matrix(y_teste, previsoes))

    frases_novas = [
        "estou com dor no peito e suor intenso",
        "tenho apenas um leve cansaço hoje",
        "estou com falta de ar e tontura",
        "sinto um pequeno incômodo muscular"
    ]

    frases_novas_tfidf = vectorizer.transform(frases_novas)
    predicoes_novas = modelo.predict(frases_novas_tfidf)

    print("\nTeste com novas frases:")
    for frase, predicao in zip(frases_novas, predicoes_novas):
        print(f"- {frase} -> {predicao}")

if __name__ == "__main__":
    main()
