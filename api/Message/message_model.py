from api import db
from datetime import datetime
from api.Tags_Messages.tag_message_table import tag_message


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    feature_image = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
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
            "feature_image": self.feature_image,
            "created_at": self.created_at,
        }
