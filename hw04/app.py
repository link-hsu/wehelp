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
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    # get POST user_id and password
    user_id = request.form["user_id"]
    password = request.form["password"]

    # check user_id and password is not null
    if not user_id or not password:
        return redirect("/error?message=請輸入帳號及密碼")
        # return redirect(url_for("error", msg="請輸入帳號及密碼"))        

    # user_id and password test
    if user_id == "test" and password == "test":
        session["user"] = user_id
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼錯誤")
        # return redirect(url_for("error", msg="帳號或密碼錯誤"))
        
        


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
    message = request.args.get("message", "")
    return render_template("error.html", message=message)

@app.route("/square/<int:number>", methods=["POST"])
def square(number):
    return render_template("square.html", number=number)

# start server
app.run(port=3000)
