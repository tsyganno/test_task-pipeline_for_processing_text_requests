from flask import Flask, request, jsonify
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

# Загрузка русского языкового пакета spaCy
nlp = spacy.load("ru_core_news_sm")

# Загрузка стоп-слов NLTK
nltk.download("stopwords")
russian_stopwords = set(stopwords.words("russian"))

# Подготовка данных для поиска (имитация БД)
documents = [
    "Это пример текста для поиска.",
    "Другой документ содержит информацию о Python.",
    "Здесь можно найти данные об обработке текста.",
    "Рандомные данные для заполнения базы данных.",
    "Победил ли Нео агента Смитта в Матрице 3?",
    "Обновленная информация."
]


def preprocess_text(text):
    # Приведение к нижнему регистру
    text = text.lower()
    # Удаление пунктуации
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Лемматизация и удаление стоп-слов
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.text not in russian_stopwords]
    return tokens


# Создание TF-IDF модели
vectorizer = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
tfidf_matrix = vectorizer.fit_transform([preprocess_text(doc) for doc in documents])


def search(query, top_n=3):
    # Поиск по тексту
    query_vector = vectorizer.transform([preprocess_text(query)])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return [documents[i] for i in top_indices]


app = Flask(__name__)


@app.route("/api/preprocess", methods=["POST"])
def api_preprocess():
    data = request.json
    text = data.get("text", "")
    tokens = preprocess_text(text)
    return jsonify({"tokens": tokens})


@app.route("/api/search", methods=["POST"])
def api_search():
    data = request.json
    query = data.get("query", "")
    results = search(query)
    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True)
