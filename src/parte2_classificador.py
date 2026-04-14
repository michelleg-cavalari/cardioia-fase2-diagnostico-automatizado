import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Carregar dados
df = pd.read_csv("data/frases_risco.csv")

# Separar dados
X = df["frase"]
y = df["situacao"]

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Transformar texto em números
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Treinar modelo
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Previsão
predictions = model.predict(X_test_tfidf)

# Avaliação
accuracy = accuracy_score(y_test, predictions)

print("Acurácia:", accuracy)

# Teste com novas frases
novas_frases = [
    "dor no peito e falta de ar",
    "leve dor nas costas",
    "tontura e coração acelerado"
]

novas_tfidf = vectorizer.transform(novas_frases)
resultados = model.predict(novas_tfidf)

print("\nTestes novos:")
for frase, resultado in zip(novas_frases, resultados):
    print(frase, "→", resultado)
