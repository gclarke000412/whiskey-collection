from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, User, Whiskey, WhiskeySchema, whiskey_schema, whiskeys_schema

api = Blueprint('api',__name__, url_prefix='/api')

# Create whiskey
@api.route('/whiskey', methods = ['POST'])
@token_required
def create_whiskey(current_user_token):
    brand = request.json['brand']
    age = request.json['age']
    rating = request.json['rating']
    flavor = request.json['flavor']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    whiskey = Whiskey(brand,age,rating,flavor,price,user_token = user_token)

    db.session.add(whiskey)
    db.session.commit()

    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

# Retrieve whiskey
@api.route('/whiskey', methods = ['GET'])
@token_required
def get_whiskeys(current_user_token):
    owner = current_user_token.token
    whiskeys = Whiskey.query.filter_by(user_token = owner).all()
    response = whiskeys_schema.dump(whiskeys)
    return jsonify(response)

# Retrieve 1 whiskey
@api.route('/whiskey/<id>', methods = ['GET'])
@token_required
def get_whiskey(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        whiskey = Whiskey.query.get(id)
        response = whiskey_schema.dump(whiskey)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token required"}),401
    
#Update Car
@api.route('/whiskey/<id>', methods = ['POST', 'PUT'])
@token_required
def update_whiskey(current_user_token, id):
    whiskey = Whiskey.query.get(id)

    whiskey.brand = request.json['brand']
    whiskey.age = request.json['age']
    whiskey.rating = request.json['rating']
    whiskey.flavor = request.json['flavor']
    whiskey.price = request.json['price']
    whiskey.user_token = current_user_token.token

    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

#Delete whiskey
@api.route('/whiskey/<id>', methods = ['DELETE'])
@token_required
def delete_whiskey(current_user_token, id):
    whiskey = Whiskey.query.get(id)
    db.session.delete(whiskey)
    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

