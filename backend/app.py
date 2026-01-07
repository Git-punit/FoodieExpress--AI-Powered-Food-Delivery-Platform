from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------- Model ----------
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    category = db.Column(db.String(50))

# ---------- Routes ----------
@app.route('/api/foods', methods=['GET'])
def get_foods():
    foods = Food.query.all()
    return jsonify([
        {"id": f.id, "name": f.name, "price": f.price, "category": f.category}
        for f in foods
    ])

@app.route('/api/foods', methods=['POST'])
def add_food():
    data = request.json
    food = Food(
        name=data['name'],
        price=data['price'],
        category=data['category']
    )
    db.session.add(food)
    db.session.commit()
    return jsonify({"message": "Food added successfully"})

@app.route('/api/recommend/<category>')
def recommend(category):
    foods = Food.query.filter_by(category=category).limit(3).all()
    return jsonify([f.name for f in foods])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

