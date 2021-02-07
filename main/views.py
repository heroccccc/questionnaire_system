from flask import request, redirect, url_for, render_template
from main import app
from main.models import User

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def import_result():
    q1_result = request.form.get('q1_radio')
    q2_result = request.form.get('q2_radio')
    q3_result = request.form.get('q3_radio')
    print(q1_result, q2_result, q3_result)
    #再読み込み等による、多重投稿防止が必要
    return redirect(url_for('main'))

#回答ページへ遷移
@app.route('/answer', methods=["GET"])
def answer_question():
    return render_template("answer.html")

#回答ページへ遷移
@app.route('/result', methods=["GET"])
def show_result():
    data = User.query.all()[0]
    return render_template("result.html", id=data.id, name=data.name, q1_result=data.q1_result, q2_result=data.q2_result, q3_result=data.q3_result)