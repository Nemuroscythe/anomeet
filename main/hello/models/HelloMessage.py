from main import database as db


class HelloMessage(db.Model):
    __tablename__ = 'hello'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.String(1000), primary_key=True)
    content = db.Column(db.String(1000))

    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __repr__(self):
        return f'{self.content}'
