from flask import Flask, request
import emoji

app = Flask(__name__)

@app.route('/service', methods=['POST'])
def service():
    data = request.get.json()
    word = data['word']
    count = data['count']

    b = word
    a = emoji.emojize(':thumbs_up:'*count)
    return a

if __name__ =='__main__':
    app.run('host=0.0.0.0:5000', debug=True)