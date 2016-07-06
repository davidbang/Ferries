Ferries
====

##Award
###Dream It Code It Win It Finalist (Samsung Global Innovation Center: Unleashing Opportunities with Technology Award)

https://dreamitcodeitwinit.wordpress.com/finalists-2015/

##Description- Project Looks Better on FireFox
 This ingenious project works to matches people's food orders with potential delivery people. When you want to get food from outside but don't want to go and get it yourelf, you can post a listing on this site that asks for someone to deliver food such as popcorn chicken from Ferries. Users will see the listing and if they can fulfill the order they will message the listing's poster and negotiate the delivery fee or accept the offer that is given. The chosen delivery person will bring the food to the appointed time and location and be reimbursed for cost and labour.
 

##Youtube Link
* http://youtu.be/MrV8DIJJg70
* Longer video- https://www.youtube.com/watch?v=teVldHOTc60

##Droplet Deployment
http://104.236.234.13/

Droplet has been taken down, deployment can be seen in last 2 minutes of longer video.
 
###Work in your branch not in master

* Update time line
* Use branches
* include setup instructions

##Roles:
=====
* Python Flask, CSS, HTML- David Bang
* Javascript & Video Editor - Anish Malhotra
* Database (Mongo) - Eric Kolbusz
* API (Yelp)- Dionis Wang

##Todo Timeline:
=======
* Eric
 * by 1/10 - Account database
  * user_auth(username, password)
  * user_exists(username)
  * user_creat(username, password, frees, lunch, rep, ordersfulfilled)
  * get_data(username,data)
 * by 1/12 - Order database
  * order_creat(orderid,username, store, food, cost, offer, preferredperiod, otherperiods, instructions)
  * get_orders(stores,periods)
 * TENTATIVE - editing and adding functionality to database as required and requested by others
* David Bang
 * by 1/11 - Set up framework for login, register, account specific pages
 * by 1/13 - Connect pages with databases
 * by 1/16- have profile and user pages ready
 * by 1/20- Order pages and routingready. Place Orders, Accept Orders, Etc.
 * by 1/23- Css (Bootstrap)
 * by 1/25 -Connecting Javascript with Pages
* Dionis Wang
 * Start API after login is done.
 * Finish API by 1/18 -> 1/25
 * Yelp Api
 * Table Display or Search Results
 * Possible Geolocation with Yelp (scrapped could not get request to go through)
* Anish Malhotra
 * Javascript after others are done
 * Videos
 * 
##APIs
* Google Maps
* Flask -
* Database -
* JavaScript -
* Html & CSS -

##Features:
* user accounts and login
* Commenting
* Google maps, yelp? Recommend places based on interests
* Allow users to add request for food.
* Allow users to post reponses and requests
* User profiles with rep and comments
* Make easy money if you have alot of free time


##Project Deadline: Done
=========

##Install Instructions:
Install Mongo, Flask, oauth2(pip install) in virtual environment
Helpful Guide to installing and activating virtual environment http://flask.pocoo.org/docs/0.10/installation/

run `pip install -r requirements.txt` while in virtual env

In the directory with app.py, run `python app.py` to launch application

========
