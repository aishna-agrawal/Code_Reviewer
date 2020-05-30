import csv
import numpy as np
import pandas as pd
from code_review import *
from predictcode import *
from flask import Flask, render_template,request

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "POST":
        req = request.form
        lang = req.get("lang")
        code = req.get("code")
        features = main(code,lang)
        if(features==-1):
            result={"Note":"Enter a valid code!"}
        else:
            CSV_filename = "<Filename>"  #Filename of the CSV file which should include outputs.
            lst= list(features.values())
            q = arr_input(lst)
            lst.append(q[0])
            #features['result']=q[0]  #Uncomment for adding result in tht output.
            result=features
            with open(CSV_filename, 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(lst)
        return render_template("reviews.html", lang =lang, code = code,res = result)

    return render_template("index.html")
    
if __name__=='__main__':
    app.run(host="0.0.0.0", port="2456") #change host and port accordingly.
