from flask import Flask, jsonify
from playsound import playsound
import multiprocessing

app = Flask(__name__)

files = ["AEIOU_01.mp3","Money.mp3"]

@app.route('/', methods=['GET'])
def home():
    return 'Hello World'
                         

@app.route('/playsound/<int:id>', methods=['GET'])
def play(id):

    file_name = files[id]
    
#     playsound('AEIOU_01.mp3',True)
    p = multiprocessing.Process(target=playsound, args=(file_name,))
    p.start()
    
    
    return jsonify({'result': 'success', 'file_name': file_name})


if __name__ == "__main__":
#     app.run(debug=True, port=5678)
    app.run(debug=False)