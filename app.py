from flask import Flask,request,url_for,redirect,render_template, flash, session
import json, urllib2
from functools import wraps
import db_helper as db
import yelp

app=Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

orderid = 0
id = 0

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template ("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if ('username' not in session):
        session ['username'] = None
    if (session.get('username') != None):
        flash ("You are already logged in!")
        return redirect("/")
    session ['username'] = None
    submit = request.args.get("submit")
    if (submit == "Submit"):
        username = request.args.get("username")
        password = request.args.get("password")
        does_account_exist = db.user_auth(username, password);
        if (does_account_exist == True):
            user = db.get_data (username)
            return redirect("/profile")
        flash ("Invalid Username or Password")
        return redirect ("/")
    return render_template ("login.html")

@app.route("/register", methods = ["POST", "GET"])
def register():
    if (session.get('username') != None):
        flash ("You are already logged in!")
        return redirect ("/profile")
    register = request.args.get("register")
    if (register == "Register"):
        username = request.args.get("username")
        password = request.args.get("password")
        does_account_exist = db.user_auth(username, password)
        if (does_account_exist == True):
            flash("Account already exists") #tried registering with taken username (None, None) is not a valid user/pass combo
            return redirect("/register")
        elif (len(username)<6):
            flash("Username too short, must be at least 6 characters") #username too short, None falls under here too
            return redirect("/register")
        else:
            db.user_creat (username, password)
            flash("Successfully registered")
            return redirect ("/")
    return render_template ("register.html") #have a button that redirects to /

@app.route("/profile", methods = ["POST", "GET"])
def profile():
    if ('username' in session):
        username = session ['username']
        return render_template ("profile.html", username = username, frees = db.get_data (username, frees), lunch = db.get_data (username, lunch), rep = db.get_data (username, rep), ordersp = db.get_data (username, ordersplaced), ordersf = db.get_data (username, ordersfulfilled), comments = db.get_data (username, comments))
    else:
        return redirect ("/login")

@app.route("/oprofile/<username>", methods = ["POST", "GET"])
def otherprofile(username): ##links from other user
    
    return render_template ("profile.html", username = username, frees = db.get_data (username, frees), lunch = db.get_data (username, lunch), rep = db.get_data (username, rep), ordersp = db.get_data (username, ordersplaced), ordersf = db.get_data (username, ordersfulfilled), comments = db.get_data (username, comments));

@app.route("/placeorder", methods = ["POST", "GET"])
def placeorder():
    submit = request.args.get("submit")
    if (submit == "Submit"):
        username = request.args.get("username")
        orderid = orderid + 1
        store = request.args.get("store")
        cost = request.args.get("cost")
        offer = request.args.get("offer")
        period1 = request.args.get("period1")
        period2 = request.args.get("period2")
        instruction = request.args.get("instruction")
        db.order_creat(orderid, username, store, food, cost, offer, period1, period2, instruction)
        return redirect ("/success")
    if ('username' in session):
        username = session ['username']
        return render_template ("placeorder.html", username = username);
    else:
        return render_template ("/login")
           
@app.route("/success/<orderid>")
def success(orderid):
    return render_template ("success.html", orderid == orderid)


@app.route("/loadorders/<id>", methods=["POST", "GET"])
def loadorder(id):
    data = db.get_all_order_data(id);
    comment = request.args.get("comment")
    submitc = request.args.get("submitc")
    if (submitc == "Submit" and comment != ""):
        db.add_comment(comment, id)
        comment = ""
        return redirect ("/loadorders/" + str(id))
    return render_template ("loadorder.html", username=  )

@app.route("/orderspec", methods=["POST", "GET"])
def specorder(): ## one is null or not
    select = request.args.get("select")
    search = request.args.get("search")
    searchsubmit = request.args.get("searchsubmit")

    if(searchsubmit == "searchsubmit"): 
        if (select == "Period"):
            orders = db.get_orders (0, search)
        elif (select == "Store"):
            orders = db.get_orders (search, 0)
        else:
            return redirect("/oprofile/" + str(search))
    return render_template ("specorder.html", orders == orders);

@app.route("/results", methods=["POST", "GET"])
def results():
    search = request.args.get("search")
    if(search):
        term = request.args.get("term")
        loc = request.args.get("loc")
        results = yelp.search("restaurant","New York");
        if(results==None):
            flash("No results came up")
        return render_template ("results.html",results=results)
    else:
        return render_template("results.html", results=None)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
