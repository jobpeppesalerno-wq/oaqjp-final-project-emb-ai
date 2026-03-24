from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response ['dominant_emotion'] == None:
        result = "Invalid text! Please try again!."
    else:
        # Return a formatted string
        text1 = "For the given statement, the system response is "
        text2 = f"'anger': {response['anger']}, "
        text3 = f"'disgust': {response['disgust']}, "
        text4 = f"'fear': {response['fear']}, "
        text5 = f"'joy': {response['joy']} and "
        text6 = f"'sadness': {response['sadness']}. "
        text7 = f"The dominant emotion is {response['dominant_emotion']}."
        result = text1 + text2 + text3 + text4 + text5 + text6 + text7

    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)