from app import db

class Puppy(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    breed = db.Column(db.String(80))
    def __init__(self, name, breed='dog'):
        self.name = name
        self.breed = breed

    def json(self):
        return {
            'name': self.name,
            'breed': self.breed,
        }