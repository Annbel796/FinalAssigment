from models import db, User, Car
from app import app

users_data = [
    {"first_name": "Anna", "last_name": "Svensson", "personal_number": "19701234-5678", "address": "Gatan 1, 123 45 Staden"},
    {"first_name": "Erik", "last_name": "Karlsson", "personal_number": "19800512-1234", "address": "Gatan 2, 543 21 Staden"},
    {"first_name": "Maria", "last_name": "Lindberg", "personal_number": "19921215-9999", "address": "Parkvägen 4, 654 32 Staden"},
    {"first_name": "Johan", "last_name": "Andersson", "personal_number": "19890202-8888", "address": "Skogsvägen 8, 789 65 Staden"},
    {"first_name": "Linda", "last_name": "Nilsson", "personal_number": "19950505-7777", "address": "Centralgatan 15, 321 89 Staden"},
    {"first_name": "Oskar", "last_name": "Bergström", "personal_number": "19831010-6666", "address": "Lillvägen 6, 543 21 Staden"},
    {"first_name": "Sofie", "last_name": "Ekström", "personal_number": "20000101-5555", "address": "Havsvägen 9, 222 33 Staden"},
    {"first_name": "David", "last_name": "Forsberg", "personal_number": "19771122-4444", "address": "Åsvägen 11, 111 22 Staden"},
    {"first_name": "Caroline", "last_name": "Håkansson", "personal_number": "19860404-3333", "address": "Brovägen 12, 434 56 Staden"},
    {"first_name": "Fredrik", "last_name": "Gustafsson", "personal_number": "19931230-2222", "address": "Solvägen 23, 987 65 Staden"}
]

cars_data = [
    {"brand": "Volvo", "model_name": "XC60", "model_year": 2020, "color": "Svart", "registration_plate": "XYZ123", "owner_index": 0},
    {"brand": "Saab", "model_name": "9-3", "model_year": 2018, "color": "Blå", "registration_plate": "ABC789", "owner_index": 1},
    {"brand": "Audi", "model_name": "A6", "model_year": 2019, "color": "Grå", "registration_plate": "DEF456", "owner_index": 2},
    {"brand": "BMW", "model_name": "X5", "model_year": 2021, "color": "Vit", "registration_plate": "GHI321", "owner_index": 3},
    {"brand": "Mercedes", "model_name": "C-Class", "model_year": 2022, "color": "Röd", "registration_plate": "JKL654", "owner_index": 4},
    {"brand": "Toyota", "model_name": "Corolla", "model_year": 2017, "color": "Silver", "registration_plate": "MNO987", "owner_index": 5},
    {"brand": "Volkswagen", "model_name": "Passat", "model_year": 2020, "color": "Blå", "registration_plate": "PQR321", "owner_index": 6},
    {"brand": "Ford", "model_name": "Focus", "model_year": 2016, "color": "Grön", "registration_plate": "STU789", "owner_index": 7},
    {"brand": "Honda", "model_name": "Civic", "model_year": 2021, "color": "Gul", "registration_plate": "VWX654", "owner_index": 8},
    {"brand": "Tesla", "model_name": "Model S", "model_year": 2023, "color": "Svart", "registration_plate": "YZA987", "owner_index": 9},
    {"brand": "Kia", "model_name": "Sportage", "model_year": 2018, "color": "Brun", "registration_plate": "BCD432", "owner_index": 1},
    {"brand": "Hyundai", "model_name": "Tucson", "model_year": 2019, "color": "Vit", "registration_plate": "EFG876", "owner_index": 2},
    {"brand": "Mazda", "model_name": "CX-5", "model_year": 2022, "color": "Blå", "registration_plate": "HIJ543", "owner_index": 3},
    {"brand": "Nissan", "model_name": "Qashqai", "model_year": 2019, "color": "Orange", "registration_plate": "KLM098", "owner_index": 4},
    {"brand": "Peugeot", "model_name": "308", "model_year": 2015, "color": "Röd", "registration_plate": "NOP765", "owner_index": 5}
]

def initialize_database():
    with app.app_context():
        db.create_all()

        if User.query.first() and Car.query.first():
            print("Data already exists. Skipping insertion.")
            return

        users = []
        for user_data in users_data:
            user = User(**user_data)
            db.session.add(user)
            users.append(user)

        db.session.commit()

        for car_data in cars_data:
            owner = users[car_data.pop("owner_index")]
            car = Car(**car_data, owner_id=owner.id)
            db.session.add(car)

        db.session.commit()
        print("Database initialized with users and cars.")

if __name__ == "__main__":
    initialize_database()

    with app.app_context():
        print("Users:", User.query.count())
        print("Cars:", Car.query.count())
        print("Car List:", [car.to_dict() for car in Car.query.all()])
