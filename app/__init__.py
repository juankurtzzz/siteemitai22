from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        return render_template("homepage.html")

    @app.route("/galeria", methods=['GET'])
    def gallery():
        return render_template("gallery.html")

    return app
