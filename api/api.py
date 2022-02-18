

#from flask import Flask, jsonify



import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template,Blueprint
api_blueprint = Blueprint('api',__name__,template_folder='templates')


@api_blueprint.route('/v1')
def my_form():
    return render_template('api/api.html')

@api_blueprint.route('/v1', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']

    if(score > 0):
        label = 'This sentence is positive'
    elif(score == 0):
        label = 'This sentence is neutral'
    else:
        label = 'This sentence is negative'

    return(render_template('api/api.html', variable=label))
