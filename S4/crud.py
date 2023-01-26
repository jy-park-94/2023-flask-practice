from basic import db, Puppy

## Create

my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

## Read
all_puppies = Puppy.query.all()
print(all_puppies)

## Select (by ID)
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

## Filters (ORM)
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

## Update
print(Puppy.query.all())

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

print(Puppy.query.all())

## Delete
puppy_frankie = Puppy.query.filter_by(name='Frankie')
db.session.delete(puppy_frankie)