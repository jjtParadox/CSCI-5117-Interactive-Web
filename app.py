from flask import Flask, jsonify, redirect, render_template, request, url_for

import db

app = Flask(__name__)


@app.before_first_request
def initialize():
    db.setup()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/survey')
def survey():
    return render_template("survey.html")


@app.route('/decline')
def decline():
    return render_template("decline.html")


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        name = request.form['name']
        participation = request.form['participation'] if 'participation' in request.form else None
        last_participated, participation_info = None, None
        if participation == 'yes':
            last_participated = request.form['last-participated'] if 'last-participated' in request.form else None
            participation_info = request.form['participation-info'] if 'participation-info' in request.form else None
        learn_more = 'learn-more' in request.form and request.form['learn-more'] == 'on'
        with db.get_db_cursor(commit=True) as cur:
            cur.execute("insert into results (name, participation, last_participated, participation_info, learn_more) values (%s, %s, %s, %s, %s)",
                        (name, participation, last_participated, participation_info, learn_more,))
    return render_template("thanks.html")


@app.route('/api/results')
def api_results():
    with db.get_db_cursor() as cur:
        cur.execute("select * from results")
        rows = cur.fetchall()
    if 'reverse' in request.args and request.args['reverse'] == 'true':
        rows = list(reversed(rows))
    results = []
    for item in rows:
        results.append(dict(item))
    return jsonify(results)


if __name__ == '__main__':
    pass
