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
#     id BIGINT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255) NOT NULL,
#     username VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     follow_count INT UNSIGNED NOT NULL DEFAULT 0,
#     time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
#     );

# CREATE TABLE message (
#     id BIGINT PRIMARY KEY AUTO_INCREMENT,
#     member_id BIGINT NOT NULL,
#     content VARCHAR(255) NOT NULL,
#     like_count INT UNSIGNED NOT NULL DEFAULT 0, 
#     time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (member_id) REFERENCES member(id)
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
        session["member_id"] = user["id"]
        session["name"] = user["name"]
        session["username"] = user["username"]
        session["password"] = user["password"]
        session["follow_count"] = user["follow_count"]
        session["member_time"] = user["time"]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/member")
def member():
    if "username" in session:
        cursor = con.cursor(dictionary = True)
        cursor.execute("SELECT message.id, message.member_id, message.content, message.time, member.name, member.username, member.password FROM message INNER JOIN member ON message.member_id = member.id ORDER BY message.time")
        messages = cursor.fetchall()
        cursor.close()
        return render_template("member.html", name = session["name"] ,messages = messages)
    else:
        return redirect("/")

@app.route("/createMessage", methods=["POST"])
def createMessage():
    content = request.form["content"]
    cursor = con.cursor()
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",
                   (session["member_id"], content))
    con.commit()
    cursor.close()
    return redirect("/member")

@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    message_id = request.form["message_id"]
    cursor = con.cursor()
    cursor.execute("DELETE FROM message WHERE id = %s",
                   (message_id,))
    con.commit()
    cursor.close()
    return redirect("/member")


@app.route("/signout")
def signout():
    if "username" in session:
        session.clear()
    return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message = message)

# start server
app.run(port = 3000)