from flask import Flask
app = Flask(__name__)
@app.route('/hiii/<int:no>')
def hello_name(no):
    return "Roll no. is %d!" %no
if __name__=='__main__':
    app.run(debug=True)
    
