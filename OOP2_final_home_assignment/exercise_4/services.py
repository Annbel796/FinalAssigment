from models import db, Car, User

class CarService:
    def create(self, brand, model_name, model_year, color, registration_plate, owner_id):
        owner = User.query.get(owner_id)
        if not owner:
            return {"error": "Owner not found"}, 404
        car = Car(
            brand=brand,
            model_name=model_name,
            model_year=model_year,
            color=color,
            registration_plate=registration_plate,
            owner_id=owner_id
        )
        db.session.add(car)
        db.session.commit()
        return car.to_dict()

    def update(self, car_id, brand=None, model_name=None, model_year=None, color=None, registration_plate=None):
        car = Car.query.get(car_id)
        if not car:
            return None
        if brand is not None:
            car.brand = brand
        if model_name is not None:
            car.model_name = model_name
        if model_year is not None:
            car.model_year = model_year
        if color is not None:
            car.color = color
        if registration_plate is not None:
            car.registration_plate = registration_plate
        db.session.commit()
        return car.to_dict()

    def delete(self, car_id):
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Car not found"}, 404
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car with id {car_id} has been deleted."}

    def get_all(self):
        cars = Car.query.all()
        for car in cars:
            print("Car from DB:", car.to_dict())
        return [car.to_dict() for car in cars]
  
    def get_by_id(self, car_id):
        car = Car.query.get(car_id)
        return car.to_dict() if car else None


class UserService:
    def create(self, first_name, last_name, personal_number, address):
        user = User(
            first_name=first_name,
            last_name=last_name,
            personal_number=personal_number,
            address=address
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    def update(self, user_id, first_name=None, last_name=None, personal_number=None, address=None):
        user = User.query.get(user_id)
        if not user:
            return None
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if personal_number is not None:
            user.personal_number = personal_number
        if address is not None:
            user.address = address
        db.session.commit()
        return user.to_dict()

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User with id {user_id} has been deleted."}

    def get_all(self):
        return [user.to_dict() for user in User.query.all()]
    
    def get_by_id(self, user_id):
        user = User.query.get(user_id)
        return user.to_dict() if user else None
    
    def get_cars_by_user(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return [car.to_dict() for car in user.cars]