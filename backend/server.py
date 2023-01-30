# Initialisation Flask
from flask import Flask


def create_app():
    application = Flask(__name__)

    application.config.from_object("backend.config.Config")

    # Import des routes
    from user.controller import blueprint as user_blueprint
    from chat.controller import blueprint as chat_blueprint
    from index.controller import blueprint as index_blueprint

    application.register_blueprint(user_blueprint)
    application.register_blueprint(chat_blueprint)
    application.register_blueprint(index_blueprint)

    return application


if __name__ == "__main__":
    application = create_app()
    application.run(host='0.0.0.0', port=80)
