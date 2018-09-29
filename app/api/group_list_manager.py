from flask import Blueprint, request
import json
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.entity.grouplist_entity import Grouplist_entity
from app.database import db

group_list_request = Blueprint('group_list_request', __name__)


# @list_Request.route("/getlistdata", methods=['POST'])
@group_list_request.route("/device/list/<account>/<group_name>", methods=['GET'])
def get_list_data(account, group_name):
    data_list = db.session.query(Grouplist_entity.listkey,Grouplist_entity.listvalue)\
        .filter(Grouplist_entity.account == account).filter(Grouplist_entity.listname == group_name).all()
    return_json_dict = dict()
    for data in data_list:
        list_key = data[0]
        list_value = data[1]
        return_json_dict[list_key] = list_value
    return json.dumps(return_json_dict, ensure_ascii=False)


def __auth_if_repeat_list(account, new_group_name):
    # 如果有重複 返回True 沒有重複返回False
    rowcount = Grouplist_entity.query.filter(Grouplist_entity.listname == new_group_name)\
        .filter(Grouplist_entity.account).count()

    return rowcount >= 1


# @list_Request.route("/insertnewdatatolist", methods=['POST'])
@group_list_request.route("/device/newdata", methods=['POST'])
def insert_newData_to_oldList():
    json_data = request.get_json()
    insert_type = json_data['insert_type']
    account = json_data['account']
    list_name = json_data['list_name']
    # data_list type is list
    list_key = json_data['list_key']
    list_value = json_data['list_value']
    group_image_uri = json_data['group_image_uri']

    list_value = list_value.replace("'", " ")
    list_value = list_value.replace(";", " ")
    # if insert_type != "extra_add":
    #     # another new_add,change_add 都一樣 先刪除 在全部加入
    #     __delete_list_data(account, list_name)
    db_execute_status =True
    try:
        grouplist_entity = Grouplist_entity(account=account, listname=list_name, listkey=list_key, listvalue=list_value,
                                            group_image_uri=group_image_uri)
        db.session.add(grouplist_entity)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        db_execute_status = False
    return json.dumps(db_execute_status, ensure_ascii=False)


def __delete_list_data(account, group_name):
    check_result = db.session.query(Grouplist_entity).filter(Grouplist_entity.account == account).filter(Grouplist_entity.listname == group_name).first()
    print(check_result)
    if check_result is not None:
        db.session.delete(check_result)
        db.session.commit()


# @list_Request.route("/getalllistdata", methods=['POST'])
@group_list_request.route("/info/<account>", methods=['GET'])
def all_get_group_data(account):
    all_group_info_data = db.session.query(Grouplist_entity.listname, (func.count('listkey')-1), Grouplist_entity.group_image_uri)\
        .filter(Grouplist_entity.account == account).all()
    return_list = []
    if all_group_info_data is not None:
        for data in all_group_info_data:
            item_json = {'listname': data[0], 'people_count': data[1], 'group_image_uri': data[2]}
            return_list.append(item_json)
    return json.dumps(return_list, ensure_ascii=False)


# @list_Request.route("/creategroup", methods=['POST'])
@group_list_request.route("/create", methods=['POST'])
def create_group():
    json_data = request.get_json()
    account = json_data.get('account')
    listname = json_data.get('listname')
    group_image_uri = json_data.get('group_image_uri')
    listname = listname.replace("'", " ")
    listname = listname.replace(";", " ")

    db_execute_status = True
    try:
        grouplist_entity = Grouplist_entity(account=account, listname=listname, listkey='', listvalue='',
                                            group_image_uri=group_image_uri)
        db.session.add(grouplist_entity)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        db_execute_status = False
    return json.dumps(db_execute_status, ensure_ascii=False)


# @list_Request.route("/deletegroup", methods=['POST'])
@group_list_request.route("/delete/<account>/<group_name>", methods=['DELETE'])
def delete_group(account, group_name):
    group = Grouplist_entity.query.filter(Grouplist_entity.account == account)\
        .filter(Grouplist_entity.listname == group_name).first()

    db_execute_status = True
    try:
        db.session.delete(group)
        db.session.commit()
    except UnmappedInstanceError:
        db.session.rollback()
        db_execute_status = False
    return json.dumps(db_execute_status, ensure_ascii=False)

# @list_Request.route("/listcount", methods=['POST'])
@group_list_request.route("/device/count/<account>/<group_name>", methods=['GET'])
def get_list_count(account, group_name):
    data_count = db.session.query(
        (func.count('*') - 1)).filter(Grouplist_entity.account == account) \
        .filter(Grouplist_entity.listname == group_name).first()
    return json.dumps(data_count[0], ensure_ascii=False)


# @list_Request.route("/alllistname", methods=['POST'])
@group_list_request.route("/name/<account>", methods=['GET'])
def get_all_list_name(account):
    all_group_name_list = db.session.query(Grouplist_entity.listname)\
        .filter(Grouplist_entity.account == account).group_by('listname').all()
    return_list = []
    if all_group_name_list is not None:
        for data in all_group_name_list:
            if data is not "":
                print(data)
                return_list.append(data[0])
    return json.dumps(return_list, ensure_ascii=False)


# @list_Request.route("/getsomegrouplistdata", methods=['POST'])
@group_list_request.route("/info/<account>/<group_name>", methods=['GET'])
def get_somegroup_list_data(account, group_name):
    all_group_name_list = db.session.query((func.count('*') - 1), Grouplist_entity.group_image_uri) \
        .filter(Grouplist_entity.account == account).group_by('listname').all()
    item_json = []
    if all_group_name_list is not None:
        for data in all_group_name_list:
            print(data)
            item_json = {'people_count': data[0], 'group_image_uri': data[1]}
    return json.dumps(item_json, ensure_ascii=False)