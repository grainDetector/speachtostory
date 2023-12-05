from flask import Flask, render_template, request, jsonify , json
import speech_recognition as sr

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
        except Exception as e:
            print('Exception: ' + str(e))

    return said

@app.route("/")
def welcome():
	return 'welcome to UserStory Generation'

    
if __name__ == "__main__":
	app.run(debug=True)
     
