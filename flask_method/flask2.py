from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('tempalte tempalte/static_text.html')
app.run(debug = True)