import uuid

from sqlalchemy.dialects.postgresql import UUID

from main import database as db


class HelloMessage(db.Model):
    __tablename__ = 'hello'
    __table_args__ = {"schema": "public"}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = db.Column(db.String(1000))

    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'{self.content}'
