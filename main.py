from flask import Flask, render_template, request, redirect, url_for, session
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use environment variable for production

## ROUTES ##
@app.route('/')
def home():
    return render_template('home.html')

## RUN THE APP ##
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Heroku's PORT variable
    app.run(debug=False, host='0.0.0.0', port=port)
