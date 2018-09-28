from app.database import db


class AccountEntity(db.Model):
    __tablename__ = 'user_info'
    account = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(70))

    def procfile_data_to_json(self):
        json = {
            'account': self.account,
            'name': self.name,
            'profile_image': self.profile_image
        }
        return json
