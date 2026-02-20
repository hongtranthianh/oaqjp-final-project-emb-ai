
"""
Emotion Detection Web Application

This module provides a Flask web application for detecting emotions in text
using the Watson NLP Emotion Detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the sentiment of the provided text.

    Retrieves text from request arguments, passes it to the emotion detector,
    and returns a formatted string with emotion scores and the dominant emotion.

    Returns:
        str: Formatted string with emotion analysis or error message
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None (indicating an error/invalid input)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract information from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template for the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
