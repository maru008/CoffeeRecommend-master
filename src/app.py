from flask import Flask, request, render_template
app= Flask(__name__)

@app.route('/')

def hello():
    return 'Hello, World!'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        return "POST로 전달"
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/hello')
def hellohtml():
    return render_template("hello.html")