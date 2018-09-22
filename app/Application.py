from flask import Flask
from app import database
from app.api.accountmanager import account_request

app = Flask(__name__)
app.register_blueprint(account_request, url_prefix="/account")


if __name__ == '__main__':
    database.db_init()
    app.run()


@app.route("/")
def hello_rollcall():
    return "Hello RollCall User"
