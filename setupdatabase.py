from APP import db, Puppy

db.create_all()

sam = Puppy("Sammy", 3)
frank = Puppy("Frankie", 4)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit()

class Owner (db.Model)

        __tablename__="Owners"

        id(db.Column(db.Integer, primary_key=True))

