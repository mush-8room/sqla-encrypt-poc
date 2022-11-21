from sqlalchemy import Column, Unicode,  String

from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from ulid import ulid

from sqla_encrypt_poc.repository.sqla.base import Base
from sqla_encrypt_poc.entrypoints.flask_app.domain.models import Identity as IdentityEntity

key = 'SuperSecret'


class Identity(Base):
    __tablename__ = "identities"

    id = Column("id", String(255), primary_key=True)
    name = Column("name", Unicode, nullable=True)
    phone_number = Column(EncryptedType(Unicode, key, AesEngine, "pkcs5"))

    def to_entity(self):
        return IdentityEntity(
            id=self.id,
            name=self.name,
            phone_number=self.phone_number,
        )

    @classmethod
    def from_entity(cls, entity: IdentityEntity):
        model = cls(
            name=entity.name,
            phone_number=entity.phone_number,
        )

        if entity.id:
            model.id = entity.id
        model.id = ulid()
        return model
