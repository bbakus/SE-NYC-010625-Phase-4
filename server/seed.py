#!/usr/bin/env python3

from app import app
from models import db, Hotel

with app.app_context():
    # Write code to seed hotels into the hotels table in the database


    Hotel.query.delete()

    hotel1 = Hotel(name="Love Shack")
    hotel2 = Hotel(name="SexLand")
    hotel3 = Hotel(name="BonerTown")
    hotel4 = Hotel(name="PenisCove")


    db.session.add_all([hotel1, hotel2, hotel3, hotel4])
    db.session.commit()

    print("🌱 Hotels successfully seeded! 🌱")