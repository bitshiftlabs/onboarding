from flask import Flask, jsonify,render_template,request
from reasons_list import Reasons
import random,re

app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home_page():
        print(request.method)
        if request.method == 'POST':
            return render_template('reason.html')
        else:
            return render_template('home.html')

@app.route('/reasons/<reason_id>')
def show_reason(reason_id):
    key=re.sub(' +', ' ', ('%s' % reason_id).lower())
    if key in Reasons:
        random_reason=random.choice(Reasons[key])
        return render_template('reason.html',value=random_reason)
    else:
        return "Error:404:Key does not exist"

if __name__=="__main__":
    app.run(debug=True)
