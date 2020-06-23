from flask import Flask, render_template, request
from src.functions import getIdea, postIdea

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',idea = "Хмм..")

@app.route('/getIdea')
def newIdea():
    return render_template('getIdea.html',idea = getIdea())
    
@app.route('/postIdea', methods=['GET', 'POST'])
def addIdea():
    if request.method == 'POST':
    	postIdea(request.form['idea'])
    return render_template('postIdea.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
