
from flask import Flask, render_template, request
import p
import pickle


app= Flask (__name__)
model = pickle.load(open('diabetic_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/",methods=["GET","POST"])
def p():
    if request.method== "POST":
        pregnancies_no=request.form["pregnancies_no"]
        Glucose_no=request.form["Glucose_no"]
        Insulin_no=request.form["Insulin_no"]
        BMI_no=request.form["BMI_no"]
        DiabetesPedigreeFunction_no=request.form["DiabetesPedigreeFunction_no"]
        Age_in_year=request.form["Age_in_year"]
        
    pred=model.predict([[pregnancies_no,Glucose_no,Insulin_no,BMI_no,DiabetesPedigreeFunction_no,Age_in_year]])
        
    if pred==[1]:
        return render_template('index.html',prediction_text="The person is a Diabetic.")
    else:
        return render_template('index.html',prediction_text="The person is Non-Diabetic.")

    
    '''return render_template("index.html", prediction_text="person is {}".format(pred))'''

'''@app.route("/sub",methods= ["post"])
 def submit():
    if request.method == "POST":
        name=request.form["username"]
    return render_template("sub.html",n=name)'''

if __name__ == "__main__":
    app.run(debug=True)





