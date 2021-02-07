from flask import request, redirect, url_for, render_template
from main import app, db
from main.models import User

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def import_result():
    user_name = request.form.get('user_name')
    q1_result = request.form.get('q1_radio')
    q2_result = request.form.get('q2_radio')
    q3_result = request.form.get('q3_radio')

    #1つでも入力されていない場合は、dbへinputさせない
    #この書き方は良くない
    if not (not user_name or q1_result == None or q2_result == None or q3_result == None):
        new_result = User(
                name = user_name,
                q1_result = q1_result,
                q2_result = q2_result,
                q3_result = q3_result
        )
        db.session.add(new_result)
        db.session.commit()

    #再読み込み等による、多重投稿防止が必要
    return redirect(url_for('main'))

#回答ページへ遷移
@app.route('/answer', methods=["GET"])
def answer_question():
    return render_template("answer.html")

#回答ページへ遷移
@app.route('/result', methods=["GET"])
def show_result():
    result_data = User.query.all()
    return render_template("result.html", result_data=result_data)