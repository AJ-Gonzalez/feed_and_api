from flask import Flask
from flask_restful import Resource, Api, reqparse
from dbutils import insertMovie, fetchMovies
from flask_cors import CORS
import feedgenerator


def updateRSS():
    feed = feedgenerator.Rss201rev2Feed(
        title="Movie Website Example",
        link="Example.com/movies",
        description="A movie blog, probably",
        language="en",
    )

    feedB = feedgenerator.Atom1Feed(
        title="Movie Website Example",
        link="Example.com/movies",
        description="A movie blog, probably"
    )

    for movie in fetchMovies():
        feed.add_item(
            title=movie[1],
            link="http://www.example.com/movies",
            description=movie[2]
        )
        feedB.add_item(
            title=movie[1],
            link="http://www.example.com/movies",
            description=movie[2]
        )

    with open('movies.rss', 'w') as fp:
        feed.write(fp, 'utf-8')
    with open("movies.ATOM", "w") as af:
        feedB.write(af, 'utf-8')


app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("title")
parser.add_argument("description")
parser.add_argument("price")
parser.add_argument("release")


class Movies(Resource):

    def post(self):
        args = parser.parse_args()
        insertMovie(args['title'], args['description'],
                    args['price'], args['release'])

        print(args)
        updateRSS()
        return 201


api.add_resource(Movies, '/addmovie')

if __name__ == '__main__':
    app.run(debug=True)
