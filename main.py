from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'
    
if __name__ == '___main__':
    app.run(debug=True)
