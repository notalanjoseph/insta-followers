from flask import Flask
from views import myviews

app = Flask(__name__)
app.register_blueprint(myviews, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # port=5000 by default



