from flask import render_template, flash, redirect, request
from app import app, db, models
from .models import Restaurant, Menu, Review
from sqlalchemy import func, distinct, or_
from .forms import SearchForm


@app.route('/', methods=['GET','POST'])
@app.route('/home/', methods=['GET','POST'])
def home ():

    form = SearchForm()
#    print(form.validate_on_submit())
#    if form.validate_on_submit():
    if request.method == 'POST':
        flash(request.form["search"])
        print(request.form["search"])
        return searchPage(request.form["search"])
    return render_template('homePage.html', form=form)

@app.route('/page/',defaults={'page':1},methods=['GET','POST'])
@app.route('/page/<int:page>',methods=['GET','POST'])
def foods(page):
    #aRestaurant = Restaurant(name='College Cafe', address='1234 Tired Lane', phone_number='(666)-666-6666')
    #myMenu1 = Menu(7, 'Chicken Caeser Salad',1,"http://www.wish-bone.com/wp-content/uploads/2013/11/GrilledChickenCaesarSalad.jpg")
    #thisReview = Review(7, 'Chicken is dry', 1)
    #if(not(db.session.query(distinct(Restaurant.id)).count() > 0)):
        #aRestaurant = Restaurant(name='College Cafe', address='1234 Tired Lane', phone_number='(666)-666-6666')
    #db.session.add(aRestaurant)
    #db.session.commit()
    #myMenu1 = Menu(7, 'Chicken Caeser Salad',0,"http://www.wish-bone.com/wp-content/uploads/2013/11/GrilledChickenCaesarSalad.jpg")
    # myMenu2 = Menu(7, 'Grilled Salmon',1,"https://www.wholefoodsmarket.com/sites/default/files/media/2555.jpg")
    # thisReview2 = Review(7, 'Salmon is dry', 1)
    # myMenu3 = Menu(7, 'Fruit Stuffed Crepe',1,"http://www.drodd.com/images12/crepe-recipe11.jpg")
    # thisReview3 = Review(7, 'Crepe is dry', 1)
    # db.session.add(myMenu2)
    # db.session.commit()
    #thisReview = Review(7, 'Chicken is dry', 0)
    # db.session.add(thisReview2)
    # db.session.commit()
    # db.session.add(myMenu3)
    # db.session.commit()
    #thisReview = Review(7, 'Chicken is dry', 0)
    # db.session.add(thisReview3)
    # db.session.commit()
    thing = Restaurant.query.filter_by(id=page).first()
    foomenu = Menu.query.filter_by(restaurant_id=thing.id)

    return render_template('restaurantPageTemplate.html',restaurantName=thing.name,foods=foomenu.all())

@app.route('/search/',defaults={'srch':""},methods=['GET','POST'])
@app.route('/search/<srch>',methods=['GET','POST'])
def searchPage(srch):
    restlist = Restaurant.query.filter(or_(Restaurant.name.ilike('%' + srch + '%'), Restaurant.address.ilike('%' + srch + '%')))
    #set(restList)
    #foomenu = Menu.query.filter_by(restaurant_id=thing.id)

    return render_template('searchPageTemplate.html',restList=restlist)
