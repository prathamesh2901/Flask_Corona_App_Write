from flask_restful import Resource, reqparse
from models.state import StateModel

class State(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)


    def post(self, name, country):
        if StateModel.find_by_state(name):
            return {"message": "A state with name '{}' already exists".format(name)}, 400

        data = State.parser.parse_args()
        state = StateModel(name, **data)
        try:
            state.save_to_db()
            return {'message': 'State created'}, 200
        except:
            return {'message': 'An Error occured while creating the state'}, 500


    def put(self, name, country):

        data = State.parser.parse_args()

        state = StateModel.find_by_country(name)

        if state is None:
            state = StateModel(name, **data)
        else:
            state.cases = data['cases']
            state.deaths = data['deaths']
            state.deaths = data['deaths']

        state.save_to_db()

        return state.json()

    def delete(self, name, country):
        state = StateModel.find_by_state(name)
        if state:
            state.delete_from_db()
            return {"message": "State '{}' Deleted".format(name)}, 200
        return {"message": "State '{}' does not exist".format(name)}, 404
