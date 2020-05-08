from db import db

class CountryModel(db.Model):

    __tablename__= 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)

    def __init__(self, name, cases, deaths, recoveries):
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries

    def json(self):
        return {'name': self.name, 'cases': self.cases, 'deaths': self.deaths, 'recoveries': self.recoveries}

    @classmethod
    def find_by_country(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
