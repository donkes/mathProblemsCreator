from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS = [
    {
        "id": "q1",
        "text": "Чему равно значение выражения 2³ · 2⁴?",
        "options": [
            ("a", "2⁷ = 128"),
            ("b", "2¹² = 4096"),
            ("c", "4⁷ = 16384"),
            ("d", "2⁻¹ = 0,5"),
        ],
        "answer": "a",
    },
    {
        "id": "q2",
        "text": "Решите уравнение: 3x − 7 = 11.",
        "options": [
            ("a", "x = 1"),
            ("b", "x = 4"),
            ("c", "x = 6"),
            ("d", "x = 18"),
        ],
        "answer": "c",
    },
    {
        "id": "q3",
        "text": "Найдите дискриминант уравнения x² − 5x + 6 = 0.",
        "options": [
            ("a", "D = 1"),
            ("b", "D = 13"),
            ("c", "D = 25"),
            ("d", "D = −1"),
        ],
        "answer": "a",
    },
    {
        "id": "q4",
        "text": "Чему равен sin 30°?",
        "options": [
            ("a", "0"),
            ("b", "1/2"),
            ("c", "√2/2"),
            ("d", "1"),
        ],
        "answer": "b",
    },
]


@app.route("/")
def index():
    return render_template("quiz.html", questions=QUESTIONS)


@app.route("/result", methods=["POST"])
def result():
    score = sum(request.form.get(question["id"]) == question["answer"] for question in QUESTIONS)
    return render_template("result.html", score=score, total=len(QUESTIONS))


if __name__ == "__main__":
    app.run(debug=True)
