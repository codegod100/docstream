from sqlalchemy import create_engine, select
from model import Blip, Base
from sqlalchemy.orm import Session, joinedload
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit


app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "secret!"

socketio = SocketIO(app, cors_allowed_origins="*")


engine = create_engine("sqlite:///blips.sql", echo=True)
Base.metadata.create_all(engine)


@app.route("/create")
def hello_world():
    with Session(engine) as session:
        blip = Blip(author="vera", content="edit me", slug="first")
        blip2 = Blip(author="test", content="wee", blips=[blip])
        session.add_all([blip, blip2])
        session.commit()
    return "<p>Hello, World!</p>"


@app.route("/select")
def sel():
    with Session(engine) as session:
        stmt = select(Blip).where(Blip.author == "test")
        for blip in session.scalars(stmt):
            print(blip.blips)
    return "OK"


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
    socketio.run(app)
