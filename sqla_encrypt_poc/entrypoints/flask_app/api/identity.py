from flask import request, jsonify

from sqla_encrypt_poc.entrypoints.flask_app.database import db
from sqla_encrypt_poc.entrypoints.flask_app.api import api
from sqla_encrypt_poc.entrypoints.flask_app.domain.models import Identity as IdentityEntity
from sqla_encrypt_poc.repository.idendity.sqla.models import Identity


@api.post('/identity')
def post_identity():
    data = request.get_json()
    identity = IdentityEntity(name=data.get("name"), phone_number=data.get("phone_number"))
    db.session.add(Identity.from_entity(identity))
    db.session.commit()

    return jsonify({"message": "post success"}), 200


@api.get('/identity')
def get_identity():

    name = request.args.get('name', None)
    if name is None:
        return jsonify({"message": "name not exist"}), 400
    user = db.session.query(Identity).filter_by(name=name).first()
    db.session.commit()
    print(user.to_entity())
    return jsonify(user.to_entity().to_dict()), 200
