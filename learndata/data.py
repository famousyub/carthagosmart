from flask import Blueprint , render_template

data_blueprint = Blueprint('data',__name__,template_folder='templates')

@data_blueprint.route("/data")
def index1():
    return "data"

@data_blueprint.route("/data_template")
def ren_tem():
    return render_template("learn.html")
