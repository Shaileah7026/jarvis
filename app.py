from flask import Flask, render_template, request
import webbrowser
from AppOpener import run
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_vs', methods=["POST"])
def button_vs():
    run('VISUAL STUDIO CODE')
    return render_template('index.html')

@app.route('/button_camera', methods=["POST"])
def button_camera():
    run('CAMERA')
    return render_template('index.html' )

@app.route('/button_chrome', methods=["POST"])
def button_chrome():
    run('GOOGLE CHROME')
    return render_template('index.html' )

@app.route('/button_firefox', methods=["POST"])
def button_photoshop():
    run('FIREFOX')
    return render_template('index.html' )

@app.route('/button_Files', methods=["POST"])
def button_Files():
    run('FILE EXPLORER')
    return render_template('index.html' )

@app.route('/button_type', methods=["POST"])
def button_type():
    run('TYPING MASTER')
    return render_template('index.html')

def main():
    webbrowser.open_new_tab('http://127.0.0.1:5000')
    app.run(debug=True)
main()


