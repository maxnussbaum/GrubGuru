from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True)
    address = db.Column(db.String(100), index=True, unique=False)
    phone_number = db.Column(db.String(20), index=True, unique=False)
    menus = db.relationship('Menu', backref='restaurant', lazy='dynamic')

    def __init__(self, name, address, phone_number):
        #self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        #self.menus = menus
#food
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_rating = db.Column(db.Integer, index=True)
    food_name = db.Column(db.String(80), index=True)
    reviews = db.relationship('Review', backref='review',lazy='dynamic')
    restaurant_id = db.Column(db.Integer, db.ForeignKey(Restaurant.id))
    image = db.Column(db.String(256))

    def __init__(self, food_rating, food_name, restaurant_id, image_string=''):
        #self.id = id
        self.food_rating = food_rating
        self.food_name = food_name
        #self.reviews = reviews
        self.restaurant_id = restaurant_id
        self.image = image_string

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer, index=True)
    comment = db.Column(db.String(250), index=True)
    menu_id = db.Column(db.Integer, db.ForeignKey(Menu.id))
    #restaurant_id = db.Column(db.Integer, db.ForeignKey(Restaurant.id ))

    def __init__(self, rating, comment, menu_id):
        #self.id = id
        self.rating = rating
        self.comment = comment
        self.menu_id = menu_id
        #self.restaurant_id = restaurant_id
