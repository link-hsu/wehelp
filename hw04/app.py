# initialize connect to database
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.j5em5lg.mongodb.net/")
db = client.memberSystem
print("database successfully connected")

# initialize flask
from flask import *
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="this is my secret"


# Routes
# root
@app.route("/")
def index():
    collection = db.user
    collection.insert_one({
        "user_id": "test",
        "password": "test"
    })
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    # get POST user_id and password
    user_id = request.form["user_id"]
    password = request.form["password"]

    # check user_id and password is not null
    if not user_id or not password:
        return redirect("/error?msg=Please enter username and password")

    # user_id and password exist
    collection = db.user
    result = collection.find_one({
        "$and":[
        {"user_id": user_id},
        {"password": password}]})
    
    # error user_id or password
    if result == None:
        return redirect("/error?msg=Username or password is not correct")
    
    # correct user_id and password
    session["user"] = result["user_id"]
    return redirect("/member")


@app.route("/member")
def member():
    if "user" in session:
        return render_template("member.html")
    else:
        return redirect("/")
    
@app.route("/signout")
def signout():
    del session["user"]
    return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("msg", "帳號或密碼發生錯誤")
    return render_template("error.html", message=message)

@app.route("/square", methods=["POST"])
def square():
    number = request.form["int"]
    return redirect(f"/square/{number}")

@app.route("/square/<number>")
def squareResult(number):
    number = int(number)
    return render_template("square.html", number=number)


# start server
app.run(port=3000)
