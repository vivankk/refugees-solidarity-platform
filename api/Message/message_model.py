from api import db
from datetime import datetime
from api.Tag_Message.tab_message_table import tag_message


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    tags = db.relationship(
        "Tag",
        secondary=tag_message,
        backref=db.backref("messages_associated", lazy="dynamic"),
    )

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
        }
