from flask import Flask, request, render_template

app= Flask(__name__)

@app.route('/')
@app.route("/index")

def index():
    return render_template("index.html")


@app.route("/index",methods=["post"])
def post():
    Aroma = request.form.get("Aroma")
    Flavor = request.form.get("Flavor")
    Aftertaste = request.form.get("Aftertaste")
    Acidity = request.form.get("Acidity")
    Sweetness = request.form.get("Sweetness")
    
    res_datas = [Aroma,Flavor,Aftertaste,Acidity,Sweetness]
    
    return render_template("index.html", okyo=res_datas)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)