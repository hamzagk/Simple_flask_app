from flask import Flask,render_template, request, flash
app=Flask(__name__) #create a class for our app
app.secret_key="123"
@app.route("/hello") # represent the last part of the URL
def index():
    flash("whats your name ?")
    flash("whats your email")
    return render_template("index.html")
@app.route("/greet",methods=["POST","GET"])
def greet():
    flash("Hi "+str(request.form['name_input'])+", Great to see you")
    flash("Your mail is = "+str(request.form['email_input']))
    return render_template("index.html")



