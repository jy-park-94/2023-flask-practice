from basic import db, Puppy

db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

print(sam.ID)
print(frank.ID)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.ID)
print(frank.ID)
