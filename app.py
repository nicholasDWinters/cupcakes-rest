"""Flask app for Cupcakes"""
from flask import Flask,request,jsonify,render_template
from models import connect_db, db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/api/cupcakes')
def all_cupcakes():
    '''get data about all cupcakes'''
    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes = serialized)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Returns JSON for specified cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Creates a new cupcake and returns JSON"""
    new_cupcake = Cupcake(
        flavor = request.json['flavor'], 
        size = request.json['size'],
        rating = request.json['rating'],
        image = request.json['image']
        )
    db.session.add(new_cupcake)
    db.session.commit()
    response = jsonify(cupcake = new_cupcake.serialize())
    return (response, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
    '''edit the specified cupcake'''
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    '''delete the specified cupcake'''
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='deleted')