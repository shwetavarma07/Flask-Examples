from flask import Flask
app=Flask(__name__)

@app.route('/hiii/<name>')
def hello_name(name):
    return 'Hello' +name
if __name__ == '__main__':
    app.run(debug=True)
    
