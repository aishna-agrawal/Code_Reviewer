# Code_reviewer
STEPS:

create a virtual environment $ py -m venv env and activate it by $ .\env\Scripts\activate
In the environment install the following libraries(flask, scikit-learn, lizard, numpy, pandas).
Change in app.py to the csv file in which output should be taken.
flask run
Requirements for running the code- all can be installed using pip

1.flask <br>
2.sklearn <br>
3.lizard <br>
4.numpy <br>
5.pandas <br>

Code is divided into 3 parts-

app.py: Flask app
code_review.py: Genrating Halstead Metrics and Cyclomatic Complexity
predict_code.py: For giving output as good or bad using trained model
Explanation:

app.py renders the HTML and CSS UI and handles the routing og templates.
app.py calls main() function in code_review.py which returns the features of user code.
code_review.py uses codeparams functions to calculate halstead metrics and Mccabe Cyclomatic complexity.
After calculating code parameters app.py call arr_input() from predictcode.py.
arr_input() predicts the output based on the code metrices.
In arr_input() function saved trained model is stored in form .sav and we use it for prediction.
