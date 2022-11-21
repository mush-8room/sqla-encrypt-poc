from dataclasses import dataclass


@dataclass
class Identity:
    id: str
    name: str
    phone_number: str

    def __init__(
            self,
            id=None,
            name="",
            phone_number="",
    ):
        self.id = id
        self.name = name
        self.phone_number = phone_number

    def to_dict(self):
        rv = {
            key: getattr(self, key)
            for key in (
                "id",
                "name",
                "phone_number",
            )
        }

        return rv
