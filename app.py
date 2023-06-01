from flask import Flask,render_template,request
import FER20 as fer20
import cv2

app = Flask(__name__)
camera=cv2.VideoCapture(0)

@app.route("/")
def hello1():
    return render_template("web1.html") 
  
@app.route("/project_pg",methods=['GET','POST'])
def hello2():
    if request.method=="POST":
        CLICK=request.form["CLICK"]
        fer20.per2()
    return render_template("project_pg.html")

@app.route("/contact_us")
def hello3():
    return render_template("know.html")  

@app.route("/project_pg")
def hello4():
    return render_template("")

if __name__=="__main__":
    app.run(debug=True)
