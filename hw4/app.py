from flask import Flask, request, jsonify
from models import db, Cook, Dish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# ----------- Cook CRUD -----------

@app.route("/cooks", methods=["POST"])
def create_cook():
    data = request.json
    cook = Cook(name=data.get("name"), experience=data.get("experience", 0))
    db.session.add(cook)
    db.session.commit()
    return jsonify(cook.to_dict()), 201

@app.route("/cooks", methods=["GET"])
def get_cooks():
    cooks = Cook.query.all()
    return jsonify([c.to_dict() for c in cooks])

@app.route("/cooks/<int:cook_id>", methods=["GET"])
def get_cook(cook_id):
    cook = Cook.query.get_or_404(cook_id)
    return jsonify(cook.to_dict())

@app.route("/cooks/<int:cook_id>", methods=["PUT"])
def update_cook(cook_id):
    cook = Cook.query.get_or_404(cook_id)
    data = request.json
    cook.name = data.get("name", cook.name)
    cook.experience = data.get("experience", cook.experience)
    db.session.commit()
    return jsonify(cook.to_dict())

@app.route("/cooks/<int:cook_id>", methods=["DELETE"])
def delete_cook(cook_id):
    cook = Cook.query.get_or_404(cook_id)
    db.session.delete(cook)
    db.session.commit()
    return jsonify({"message": "Повар удалён"})


# ----------- Dish CRUD -----------

@app.route("/dishes", methods=["POST"])
def create_dish():
    data = request.json
    dish = Dish(
        name=data.get("name"),
        description=data.get("description"),
        price=data.get("price", 0.0)
    )
    db.session.add(dish)
    db.session.commit()
    return jsonify(dish.to_dict()), 201

@app.route("/dishes", methods=["GET"])
def get_dishes():
    dishes = Dish.query.all()
    return jsonify([d.to_dict() for d in dishes])

@app.route("/dishes/<int:dish_id>", methods=["GET"])
def get_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    return jsonify(dish.to_dict())

@app.route("/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    data = request.json
    dish.name = data.get("name", dish.name)
    dish.description = data.get("description", dish.description)
    dish.price = data.get("price", dish.price)
    db.session.commit()
    return jsonify(dish.to_dict())

@app.route("/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    db.session.delete(dish)
    db.session.commit()
    return jsonify({"message": "Блюдо удалено"})


if __name__ == "__main__":
    app.run(debug=True)
