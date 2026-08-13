from splent_framework.blueprints.base_blueprint import create_blueprint

map_bp = create_blueprint(__name__)


def init_feature(app):
    pass


def inject_context_vars(app):
    return {}
