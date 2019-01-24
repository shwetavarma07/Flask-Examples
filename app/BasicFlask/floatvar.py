from flask import Flask
app = Flask(__name__)
@app.route('/hiii/<float:no>')
def hello_name(no):
    return "Temperature is %f!" %no
if __name__=='__main__':
    app.run(debug=True)
    
