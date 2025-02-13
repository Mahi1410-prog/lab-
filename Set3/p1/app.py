from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"


@app.route ('/home')
def home():
    list1 = [1,2,3,4,5,6]
    list2 = [{"name":"Tirth","roll_no":48},{"name":"Ved","roll_no":49},{"name":"Het","roll_no":51},{"name":"Mahi","roll_no":38}]
    return render_template ('index.html',data=list2)


if __name__ == "__main__":


  app.run()