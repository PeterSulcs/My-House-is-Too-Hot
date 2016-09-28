from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class PostMeasurement(Resource):
    def post(self):
        try:
            # parse the arguments
            parser = reqparse.RequestParser()

            parser.add_argument('name', type=str, 
                help='Unique name of sensor', required=True)

            parser.add_argument('value', type=float, 
                help='The measurement value', required=True)

            parser.add_argument('timestamp', type=str, 
                help='The time and date of the measurement in format "YYYY-MM-DD HH:MM:SS"', required=True)
            args = parser.parse_args()
            _measurementName = args['name']
            _measurementValue = args['value']
            _measurementTimestamp = args['timestamp']
        except Exception as e:
            return {'error': str(e)}

        return {'name': args['name'], 'value': args['value'], 'timestamp': args['timestamp']}

class GetSensor(Resource):
    def get(self, sensor_name):
        # try:
        #     parser = reqparse.RequestParser()
        #     parser.add_argument('name', type=str, help='Unique name of sensor', required=True)

        #     # TODO: add date limits, or last number of points etc to limit data volume returned
        #     args = parser.parse_args()
        #     _sensor = args['name']

        # except Exception as e:
        #     return {'error': str(e)}

        return {'name': sensor_name}

api.add_resource(PostMeasurement, '/PostMeasurement')
api.add_resource(GetSensor, '/GetSensor/<string:sensor_name>')

if __name__ == '__main__':
    app.run(debug=True)

