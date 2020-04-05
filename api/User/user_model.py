from api import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    date_of_birth = db.Column(db.DateTime(), nullable=False)
    primary_language = db.Column(db.String(15), nullable=False)
    other_languages = db.Column(db.String(120), nullable=True)
    mobile_phone_number = db.Column(db.String(15), nullable=False)
    nationality = db.Column(db.String(75), nullable=False)
    country_of_origin = db.Column(db.String(75), nullable=True)
    swiss_permit_type = db.Column(db.String(10), nullable=True)
    current_refugee_center = db.Column(db.String(15), nullable=True)
    current_accommodation_type = db.Column(db.String(15), nullable=True)
    date_of_entry = db.Column(db.DateTime(), nullable=False)
    # canton = db.Column(db.String(2), nullable=True)
    civil_status = db.Column(db.String(15), nullable=False)
    number_of_children = db.Column(db.Integer, nullable=False)
    family_members = db.Column(db.String(120), nullable=True)
    corona_status = db.Column(db.String(75), nullable=True)
    other_health_issues = db.Column(db.Boolean(), nullable=False)
    education_level = db.Column(db.String(10), nullable=False)
    skills = db.Column(db.String(255), nullable=True)
    personality = db.Column(db.String(25), nullable=True)
    service_offered = db.Column(db.String(255), nullable=True)
    services_needed = db.Column(db.String(120), nullable=True)
    resources_available = db.Column(db.String(120), nullable=True)
    disability = db.Column(db.Boolean(), nullable=False)

    messages = db.relationship("Message", back_ref="author", lazy=True)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "email": self.id,
            "name": self.name,
            "surname": self.surname,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "primary_language": self.primary_language,
            "other_languages": self.other_languages,
            "mobile_phone_number": self.mobile_phone_number,
            "nationality": self.nationality,
            "country_of_origin": self.country_of_origin,
            "swiss_permit_type": self.swiss_permit_type,
            "current_refugee_center": self.current_refugee_center,
            "current_accommodation_type": self.current_accommodation_type,
            "date_of_entry": self.date_of_entry,
            "civil_status": self.civil_status,
            "number_of_children": self.number_of_children,
            "family_members": self.family_members,
            "corona_status": self.corona_status,
            "other_health_issues": self.other_health_issues,
            "education_level": self.education_level,
            "skills": self.skills,
            "personality": self.personality,
            "service_offered": self.service_offered,
            "services_needed": self.services_needed,
            "resources_available": self.resources_available,
            "disability": self.disability,
        }
