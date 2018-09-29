from flask import Blueprint
import json
from app.entity.todo_entity import ToDoEntity
from app.database import db
from flask import request

todo_request = Blueprint('todo_request', __name__)


@todo_request.route("/list/<account>", methods=['GET'])
def get_todo_data(account):

    todo_list = db.session.query(ToDoEntity.todo_title, ToDoEntity.todo_createtime, ToDoEntity.todo_isFinsh).filter(ToDoEntity.account == account).all()
    json_list = []
    if todo_list is not None:
        for data in todo_list:
            item_json = {'todo_title': data[0], 'todo_createtime': data[1], 'todo_isFinsh': data[2]}
            json_list.append(item_json)
    return json.dumps(json_list, ensure_ascii=False)


@todo_request.route("/create", methods=['POST'])
def create_new_todo():
    json_data = request.get_json()
    account = json_data.get('account')
    todo_title = json_data.get('todo_title')
    todo_createtime = json_data.get('todo_createtime')
    todo_title = todo_title.replace("'", "")
    todo_title = todo_title.replace(";", " ")
    db_execute_status = True
    grouplist_entity = ToDoEntity(account=account, todo_title=todo_title,
                                      todo_createtime=todo_createtime, todo_isFinsh=0)

    db.session.add(grouplist_entity)
    db.session.commit()
    return json.dumps(db_execute_status, ensure_ascii=False)


@todo_request.route("/finish", methods=['PATCH'])
def finsh_todo():
    json_data = request.get_json()
    account = json_data.get('account')
    todo_title = json_data.get('todo_title')
    todo_createtime = json_data.get('todo_createtime')
    todo_isFinsh = json_data.get('todo_isFinsh')

    ToDoEntity.query.filter_by(account=account).filter_by(todo_title=todo_title)\
        .filter_by(todo_createtime=todo_createtime).update({'todo_isFinsh': todo_isFinsh})
    db.session.commit()
    return json.dumps(True, ensure_ascii=False)


@todo_request.route("/content", methods=['PUT'])
def update_todo_content():
    json_data = request.get_json()
    account = json_data.get('account')
    new_todo_title = json_data.get('new_todo_title')
    old_todo_title = json_data.get('old_todo_title')
    new_todo_createtime = json_data.get('new_todo_createtime')
    ToDoEntity.query.filter(ToDoEntity.account == account).filter(ToDoEntity.todo_title == old_todo_title)\
        .update({'todo_title': new_todo_title, 'todo_createtime': new_todo_createtime})
    db.session.commit()
    return json.dumps(True, ensure_ascii=False)


@todo_request.route("/<account>/<todo_title>", methods=['DELETE'])
def delete_todo(account, todo_title):
    db.session.query(ToDoEntity).filter_by(todo_title=todo_title).filter_by(account=account).delete()
    db.session.commit()
    return json.dumps(True, ensure_ascii=False)