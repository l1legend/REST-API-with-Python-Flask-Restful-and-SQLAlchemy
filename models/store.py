from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') #do not go to items database and create an object for each item yet. 

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod 
    def find_by_name(cls, name): #classmethod because it is going to return an object of ItemModel as opposed to a dictionary.
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1;
        #return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):   #handles insert and update operation
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
