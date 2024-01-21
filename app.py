from emmett import App, request, response
from emmett.orm import Database, Model, Field, belongs_to, has_many
from emmett.tools import service
import json

app = App(__name__)


class Blip(Model):
    content = Field.string()
    author = Field.string()
    belongs_to("Blip")
    has_many({"blips": "Blip"})


app.config.db.uri = "sqlite:///data/blips.sql"
db = Database(app)
db.define_models(Blip)
app.pipeline = [db.pipe]


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
    author = request.args.get("author") or request.access_route[0]
    blips = Blip.where(lambda b: b.slug == slug)
    if len(blips) == 0:
        blip = Blip.create(author=author, content="edit me", slug=slug)
        blips.append(blip)
    new_blips = []
    for blip in blips:
        new_blips.append(child_blips(blip))
    blips = json.dumps(new_blips)
    return dict(author=author, blips=blips, slug=slug)


@app.route("/doc/<slug>")
@service.json
async def doc(slug):
    author = request.args.get("author")
    blips = Blip.where(lambda b: b.slug == slug)
    if len(blips) == 0:
        blip = Blip.create(author=author, content="edit me", slug=slug)
    new_blips = []
    for blip in blips:
        new_blips.append(child_blips(blip))
    data = new_blips
    return {"data": data}


# create new blip and add set slug to page
@app.route("/new/<slug>", methods=["POST"])
def new(slug):
    data = request.get_json()
    new_blip = Blip.create(content=data["content"], author=data["author"], slug=slug)
    new_blip_id = new_blip.id
    return str(new_blip_id)


# adds sub blips to a blip
@app.route("/add/<id>", methods=["POST"])
def add(id):
    data = request.get_json()
    blip = Blip.where(lambda b: b.id == id).first()
    new_blip = Blip.create(content=data["content"], author=data["author"], blips=[])
    blip.blips.append(new_blip)
    blip.save()
    new_blip_id = new_blip.id
    return str(new_blip_id)


# delete blip by id
@app.route("/remove/<id>", methods=["POST"])
def remove(id):
    blip = Blip.where(lambda b: b.id == id).first()
    blip.delete()
    return "OK"


@app.route("/edit/<id>", methods=["POST"])
def edit(id):
    data = request.get_json()
    blip = Blip.where(lambda b: b.id == id).first()
    blip.content = data["content"]
    blip.save()
    return "OK"


# @socketio.on("content")
# def handle_content(content):
#     print("Got content", content)
#     emit("content", "ok", broadcast=True)


# if __name__ == "__main__":
#     socketio.run(app, allow_unsafe_werkzeug=True)


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
