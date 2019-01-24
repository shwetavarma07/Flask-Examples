from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Shweta"
    return render_template('h.html') +name
if __name__ == '__main__':
    app.run(debug=True)
