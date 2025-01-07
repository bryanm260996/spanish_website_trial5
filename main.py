from flask import Flask, render_template, request, redirect, url_for, session



# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions


## ROUTES ##
@app.route('/')
def home():
    return render_template('home.html')



## RUN THE APP ##
if __name__ == '__main__':
    app.run(debug=True)
