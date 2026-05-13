from flask import Flask, request, render_template_string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------- Training Data ----------------
texts = [
    "I love this product",
    "This is amazing",
    "Very good experience",
    "I am happy",
    "Excellent work",
    "I hate this",
    "Very bad service",
    "Worst experience",
    "This is terrible",
    "I am sad"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]

# ---------------- Model Training ----------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis Project</title>
</head>
<body>

<h1>AI Sentiment Analysis</h1>

<form method="POST">
    <textarea name="text" placeholder="Enter Text"></textarea><br><br>
    <button type="submit">Analyze</button>
</form>

{% if result %}
    <h2>{{result}}</h2>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]

        data = vectorizer.transform([text])
        prediction = model.predict(data)[0]

        result = "Predicted Sentiment : " + prediction

    return render_template_string(HTML, result=result)

# ---------------- Run App ----------------
if __name__ == "__main__":
    app.run(debug=True)
