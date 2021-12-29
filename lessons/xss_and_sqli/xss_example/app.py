from db import get_comments, insert_comment
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        insert_comment(request.form['comment'])
        
    comments = get_comments()
    return render_template('index.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)