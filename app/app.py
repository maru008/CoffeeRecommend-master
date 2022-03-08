from flask import Flask, request, render_template
import numpy as np
from scipy.stats import zscore
import pandas as pd

app= Flask(__name__)

@app.route('/')
@app.route("/index")

def index():
    return render_template("index.html")


@app.route("/index",methods=["post"])
def post():
    #ユーザ入力の値を受け取る
    Aroma = float(request.form.get("Aroma"))
    Flavor = float(request.form.get("Flavor"))
    Aftertaste = float(request.form.get("Aftertaste"))
    Acidity = float(request.form.get("Acidity"))
    Sweetness = float(request.form.get("Sweetness"))
    
    user_coffee_val = [Aroma,Flavor,Aftertaste,Acidity,Sweetness]
    # ユーザが選んだコーヒー変数を正規化
    norm_user_coffee_val = np.array(zscore(user_coffee_val))
    
    data = pd.read_csv("app/static/data/norm_data.csv",index_col=0)
    
    res_df = pd.DataFrame(columns=["Species","Country","error"])
    for row in data.index:
        Species = list(data.loc[row])[0]
        Country = list(data.loc[row])[1]
        x_ls = np.array(list(data.loc[row])[2:2+len(norm_user_coffee_val)])
        
        coffee_error_ls = abs(norm_user_coffee_val - x_ls)
        coffee_error_sum = sum(coffee_error_ls)
        add_ls = [Species,Country,coffee_error_sum]
        res_df.loc[row] = add_ls
    sort_res_df = res_df.sort_values('error')
    
    return render_template("result.html", res = sort_res_df["Country"])

#推薦結果から元に戻る処理
@app.route("/back",methods = ["POST"])
def back():
    return render_template("index.html")

#おまじない
if __name__ == "__main__":
    app.run(debug=True)