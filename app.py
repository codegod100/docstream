import json
import random
from sqlalchemy import create_engine, select
from model import Blip, Base
from sqlalchemy.orm import Session, joinedload
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit


app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "secret!"

socketio = SocketIO(app, cors_allowed_origins="*")


engine = create_engine("sqlite:///blips.sql", echo=True)
Base.metadata.create_all(engine)


def child_blips(blip):
    data = {
        "id": blip.id,
        "author": blip.author,
        "content": blip.content,
    }
    if blip.blips:
        data["blips"] = [child_blips(b) for b in blip.blips]
    else:
        data["blips"] = []
    return data


@app.route("/d/<slug>")
def index(slug):
    author = request.args.get("author") or request.remote_addr
    blips = []
    with Session(engine) as session:
        stmt = select(Blip).where(Blip.slug == slug)
        blip = session.scalars(stmt).first()
        if not blip:
            blip = Blip(author=author, content="edit me", slug=slug)
            session.add_all([blip])
            session.commit()
        blips = json.dumps([child_blips(blip)])
    return render_template("index.html", author=author, blips=blips, slug=slug)


@app.route("/assets/<path:path>")
def send_js(path):
    return send_from_directory("templates/assets", path)


@app.route("/doc/<slug>")
def doc(slug):
    author = request.args.get("author")
    with Session(engine) as session:
        stmt = select(Blip).where(Blip.slug == slug)
        blip = session.scalars(stmt).first()
        if not blip:
            blip = Blip(author=author, content="edit me", slug=slug)
            session.add_all([blip])
            session.commit()
        data = child_blips(blip)
    return jsonify(data)


@app.route("/add/<id>", methods=["POST"])
def add(id):
    data = request.get_json()
    with Session(engine) as session:
        stmt = select(Blip).where(Blip.id == id)
        blip = session.scalars(stmt).first()
        new_blip = Blip(content=data["content"], author=data["author"], blips=[])
        blip.blips.append(new_blip)
        session.commit()
        new_blip_id = new_blip.id
    return str(new_blip_id)


@app.route("/remove/<id>", methods=["POST"])
def remove(id):
    with Session(engine) as session:
        stmt = select(Blip).where(Blip.id == id)
        blip = session.scalars(stmt).first()
        session.delete(blip)
        session.commit()
    return "OK"


@app.route("/edit/<id>", methods=["POST"])
def edit(id):
    data = request.get_json()
    with Session(engine) as session:
        stmt = select(Blip).where(Blip.id == id)
        blip = session.scalars(stmt).first()
        blip.content = data["content"]
        session.commit()
    return "OK"


@socketio.on("content")
def handle_content(content):
    print("Got content", content)
    emit("content", "ok", broadcast=True)


if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)


def generate_username():
    words = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "iceberg",
        "jackfruit",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "pineapple",
        "quince",
        "raspberry",
        "strawberry",
        "tangerine",
        "ugli",
        "victoria",
        "watermelon",
        "xigua",
        "yellow",
        "zucchini",
    ]
    username = (
        words[random.randint(0, len(words) - 1)]
        + words[random.randint(0, len(words) - 1)]
    )
    return username
