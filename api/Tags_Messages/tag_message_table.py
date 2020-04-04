from api import db

tag_message = db.Table(
    "tag_message",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("message_id", db.Integer, db.ForeignKey("message.id"), primary_key=True),
)
