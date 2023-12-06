from flask import Flask, render_template, request, jsonify , json
import speech_recognition as sr
from storygeneration import storygen
app = Flask(__name__)

@app.route("/storygeneration", methods=['GET'])
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
            req_output = storygen(said)
        except Exception as e:
            print('Exception: ' + str(e))

    return req_output


@app.route("/")
def welcome():
	return 'welcome to UserStory Generation'


if __name__ == "__main__":
	app.run(debug=True)
     
