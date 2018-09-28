from app.database import db


class Grouplist_entity(db.Model):
    __tablename__ = 'user_list_info'
    account = db.Column(db.String(30), primary_key=True, nullable=False)
    listname = db.Column(db.String(30),  primary_key=True, nullable=False)
    listkey = db.Column(db.String(20), primary_key=True, nullable=False)
    listvalue = db.Column(db.String(20))
    group_image_uri = db.Column(db.String(60))

    def group_data_to_json(self):
        json = {
            'account': self.account,
            'listname': self.listname,
            'listkey': self.listkey,
            'listvalue': self.listvalue,
            'group_image_uri': self.group_image_uri
        }
        return json