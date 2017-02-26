from flask import render_template, flash, redirect
from app import app, db, models
from .models import Restaurant, Menu, Review
from sqlalchemy import func, distinct




@app.route('/haha', methods=['GET','POST'])
def home():

    aRestaurant = Restaurant(name='College Cafe', address='1234 Tired Lane', phone_number='(666)-666-6666')
    myMenu1 = Menu(7, 'Chicken Caeser Salad',0,"http://www.wish-bone.com/wp-content/uploads/2013/11/GrilledChickenCaesarSalad.jpg")
    thisReview = Review(7, 'Chicken is dry', 0)
    if(not(db.session.query(distinct(Restaurant.id)).count() > 0)):
        #aRestaurant = Restaurant(name='College Cafe', address='1234 Tired Lane', phone_number='(666)-666-6666')
        db.session.add(aRestaurant)
        db.session.commit()
        #myMenu1 = Menu(7, 'Chicken Caeser Salad',0,"http://www.wish-bone.com/wp-content/uploads/2013/11/GrilledChickenCaesarSalad.jpg")
        db.session.add(myMenu1)
        db.session.commit()
        #thisReview = Review(7, 'Chicken is dry', 0)
        db.session.add(thisReview)
        db.session.commit()
    return render_template('base.html',restaurantName=aRestaurant.name,foods=myMenu1.query.all())
