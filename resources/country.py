from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.country import CountryModel


class Country(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)

    def post(self, name):
        if CountryModel.find_by_country(name):
            return {"message": "An country with the name '{}' already exist.".format(name)}, 400

        data = Country.parser.parse_args()

        country = CountryModel(name, **data)
        try:
            country.save_to_db()
        except:
            return {"message": "An error occured while inserting the country."}, 500

        return country.json(), 201


    def delete(self, name):
        country = CountryModel.find_by_country(name)
        if country:
            country.delete_from_db()
            return {"message": "Country '{}' deleted".format(name)}, 200
        return {"message": "Country '{}' not found".format(name)}, 404

    def put(self, name):

        data = Country.parser.parse_args()

        country = CountryModel.find_by_country(name)

        if country is None:
            country = CountryModel(name, **data)
        else:
            country.cases = data['cases']
            country.deaths = data['deaths']
            country.deaths = data['deaths']

        country.save_to_db()

        return country.json()
