from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/muslims')
def jews():
        return render_template('jew.html')

if __name__ in "__main__":
        app.debug = False
        app.run('0.0.0.0', port=80)
