from flask import Flask, jsonify, request
from models import db, Car, User
from services import CarService, UserService
import os

app = Flask(__name__)

db_path = os.path.join(os.getcwd(), "instance", "database.db")

if not os.path.exists(db_path): 
    open(db_path, 'w').close()

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# === Car endpoints ===

@app.route('/cars', methods=['GET'])
def get_cars():
    cars = CarService().get_all()
    return jsonify(cars), 200

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = CarService().get_by_id(car_id)
    return jsonify(car) if car else (jsonify({'message': 'Car not found'}), 404)

@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    new_car = CarService().create(data)
    return jsonify(new_car), 201 if new_car else (jsonify({"message": "Owner not found"}), 404)

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    updated_car = CarService().update(car_id, data)
    return jsonify(updated_car) if updated_car else (jsonify({'message': 'Car not found'}), 404)

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    deleted_message = CarService().delete(car_id)
    return jsonify({'message': deleted_message}) if deleted_message else (jsonify({'message': 'Car not found'}), 404)

# === User endpoints ===

@app.route('/users', methods=['GET'])
def get_users():
    users = UserService().get_all()
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService().get_by_id(user_id)
    return jsonify(user) if user else (jsonify({'message': 'User not found'}), 404)

@app.route('/users/<int:user_id>/cars', methods=['GET'])
def get_user_cars(user_id):
    cars = UserService().get_cars_by_user(user_id)
    return jsonify(cars), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = UserService().create(data)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserService().update(user_id, data)
    return jsonify(updated_user) if updated_user else (jsonify({'message': 'User not found'}), 404)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_message = UserService().delete(user_id)
    return jsonify({'message': deleted_message}) if deleted_message else (jsonify({'message': 'User not found'}), 404)

@app.route('/')
def hello():
    return 'Välkommen till API för användare och bilar!'

if __name__ == '__main__':
    app.run(debug=True)