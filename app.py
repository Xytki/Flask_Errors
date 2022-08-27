from flask import Flask, send_from_directory, Blueprint, request

from loader.views_loader import loader_blueprint
from main.views_main import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(loader_blueprint)
app.register_blueprint(main_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
