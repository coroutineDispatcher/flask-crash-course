from flask_restful import Resource, reqparse

from models.usermodel import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="username is required")
    parser.add_argument('password', type=str, required=True, help="password is required")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(username=data['username']):
            return {'message': 'This username already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User create successfuly'}, 201
