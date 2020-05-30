# Code Reviewer #
## STEPS: ##

1.Create a virtual environment <code> $ py -m venv env </code> and activate it by <code> $ .\env\Scripts\activate </code> <br/>
2.In the environment install the following libraries(flask, scikit-learn, lizard, numpy, pandas). <br/>
3.Change in app.py to the csv file in which output should be taken.<br/>
4.Run<code>$ python app.py</code><br/>
- - - -
## Requirements for running the code- all can be installed using pip ##

1. flask <br>
2. sklearn <br>
3. lizard <br>
4. numpy <br>
5. pandas <br>
- - - -
## Code is divided into 3 parts- ##

* app.py: Flask app <br/>
* code_review.py: Genrating Halstead Metrics and Cyclomatic Complexity <br/>
* predict_code.py: For giving output as good or bad using trained model <br/>
- - - -
## Explanation: ## 

* app.py renders the HTML and CSS UI and handles the routing og templates.<br/>
* app.py calls main() function in code_review.py which returns the features of user code.<br/>
* code_review.py uses codeparams functions to calculate halstead metrics and Mccabe Cyclomatic complexity.<br/>
* After calculating code parameters app.py call arr_input() from predictcode.py.<br/>
* arr_input() predicts the output based on the code metrices.<br/>
* In arr_input() function saved trained model is stored in form .sav and we use it for prediction.<br/>
