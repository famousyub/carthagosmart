#machleaarn
from flask import Blueprint , render_template
config_blueprint = Blueprint('configs',__name__,template_folder='templates')

@config_blueprint.route("/configs")
def configs():
    return "configs"
