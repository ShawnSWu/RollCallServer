from flask import Flask
from app import database
from app.api.accountmanager import account_request
from app.api.group_list_manager import group_list_request
from app.api.todomanager import todo_request


app = Flask(__name__)
app.register_blueprint(account_request, url_prefix="/account")
app.register_blueprint(group_list_request, url_prefix="/group_list")
app.register_blueprint(todo_request, url_prefix="/todo")


if __name__ == '__main__':
    database.db_init()
    app.run()


@app.route("/")
def hello_rollcall():
    return "Hello RollCall User"
