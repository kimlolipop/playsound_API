from flask import Flask, jsonify
# from playsound import playsound
from pygame import mixer
import multiprocessing

app = Flask(__name__)

mixer.init()
files = ["AEIOU_01.mp3","Money.mp3"]


@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/playsound/<sound_name>', methods=['GET'])
def play(sound_name):
    mixer.music.load(sound_name)
    mixer.music.play()
    print('play sound: ', sound_name)

    
    
    return jsonify({'result': 'success', 'file_name': sound_name})


if __name__ == "__main__":
#     app.run(debug=True, port=5678)
    app.run(host='0.0.0.0', debug=False,port=5678)