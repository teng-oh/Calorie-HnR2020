from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("static\data\\food-items.csv")
data_dict = {col: list(data[col]) for col in data.columns}

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        try:
            calories = data_dict.get(request.form)
        except:
            calories = ""
        return render_template("home.html", response = calories)
    else:
        return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)