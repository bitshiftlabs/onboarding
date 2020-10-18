from flask import Flask, jsonify,render_template
from reasons_list import Reasons
import random,re

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/reasons')
def show_all_problems_and_reasons():
    return jsonify(Reasons)

@app.route('/reasons/<reason_id>')
def show_reason(reason_id):
    key=re.sub(' +', ' ', ('%s' % reason_id).lower())
    if key in Reasons:
        random_reason=random.choice(Reasons[key])
        return jsonify(random_reason)
    else:
        return "Error:404:Key does not exist"

if __name__=="__main__":
    app.run(debug=True)
