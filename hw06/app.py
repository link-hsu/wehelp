from flask import *
import mysql.connector

# initialize flask
app = Flask(
    __name__,
    static_folder = "public",
    static_url_path = "/")

app.secret_key = "this is my secret"


# 在mySQL建立member & message 兩個table
# CREATE DATABASE member;
# USE member;

# CREATE TABLE member (
#     username VARCHAR(255) UNIQUE PRIMARY KEY NOT NULL,
#     name VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NOT NULL
# );

# CREATE TABLE message (
#     messageId BIGINT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(255) NOT NULL,
#     content VARCHAR(255) NOT NULL,
#     FOREIGN KEY (username) REFERENCES member(username)
# );

# connect model
con = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database="member")

# route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    cursor = con.cursor()
    cursor.execute("SELECT * FROM member WHERE username = %s", (username,))
    check_username = cursor.fetchone()
    if check_username:
        cursor.close()
        return redirect("/error?message=帳號已經被註冊")
    else:
        cursor.execute("INSERT INTO member( name, username, password) VALUES (%s, %s, %s)",
                       (name, username, password))
        con.commit()
        cursor.close()
    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    cursor = con.cursor(dictionary = True)
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s",
                   (username, password))
    user = cursor.fetchone()
    cursor.close()
    
    if user:
        session["name"] = user["name"]
        session["username"] = user["username"]
        session["password"] = user["password"]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/member")
def member():
    if "username" in session:
        cursor = con.cursor(dictionary = True)
        cursor.execute("SELECT * FROM message INNER JOIN member ON message.username = member.username ORDER BY messageId")
        messages = cursor.fetchall()
        cursor.close()
        return render_template("member.html", name = session["name"] ,messages = messages)
    else:
        return redirect("/")

@app.route("/createMessage", methods=["POST"])
def createMessage():
    content = request.form["content"]
    cursor = con.cursor()
    cursor.execute("INSERT INTO message (username, content) VALUES (%s, %s)",
                   (session["username"], content))
    con.commit()
    cursor.close()
    return redirect("/member")

@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    messageId = request.form["messageId"]
    cursor = con.cursor()
    cursor.execute("DELETE FROM message WHERE messageId = %s AND username = %s",
                   (messageId, session["username"]))
    con.commit()
    cursor.close()
    return redirect("/member")


@app.route("/signout")
def signout():
    if "username" in session:
        del session["username"]
    return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message = message)

# start server
app.run(port = 3000)