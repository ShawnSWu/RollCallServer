from flask import Blueprint
import hashlib, json, re
from flask import request
from sqlalchemy import func

from app import database
from app.entity.account_entity import AccountEntity
from app.entity.grouplist_entity import Grouplist_entity
from app.database import db


account_request = Blueprint('account_request', __name__)

ACCOUNT_IS_NOT_EXIST = 'account is not exist'
REPEAT_ACCOUNT = 'repeat account'
ACCOUNT_TYPE_IS_NOT_ALLOW = 'account type is not an allowed specifications'
SUCCESS = 'success'

SIGNUP_SUCCESS = 'Signup Success'
SIGNUP_FAIL = "Signup Fail"

SUCCESS_BOOLEAN = True
FAIL_BOOLEAN = False


def validate_email(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
        else:
            return False
    return False


def auth_account(account, sha256_password):
    if validate_email(str(account)) is not True:
        return ACCOUNT_TYPE_IS_NOT_ALLOW
    else:
        account_entity = AccountEntity.query.filter_by(account=account).first()
        if account_entity is None:
            return SUCCESS_BOOLEAN
        return SUCCESS_BOOLEAN


@account_request.route("/login", methods=['POST'])
def login():
    json_data = request.get_json()
    account = json_data.get('account')
    password = json_data.get('password')
    sha256_password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    return json.dumps(auth_account(account, sha256_password), ensure_ascii=False)


@account_request.route("/signup", methods=['POST'])
def signup():
    json_data = request.get_json()
    account = json_data.get('account')
    password = json_data.get('password')
    name = json_data.get('name')
    profile_image = json_data.get('profile_image')
    name.encode('utf-8')
    sha256_password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    result = auth_account(account, sha256_password)
    if result == ACCOUNT_IS_NOT_EXIST:
        return_message = SIGNUP_SUCCESS
        account_entity = AccountEntity(account=account, password=sha256_password, name=name, profile_image=profile_image)
        database.add_data(account_entity)
    else:
        return_message = REPEAT_ACCOUNT
    return json.dumps(return_message, ensure_ascii=False)


@account_request.route("/profile/<account>", methods=['GET'])
def get_procfile_data(account):
    procfile_data = AccountEntity.query.filter(AccountEntity.account == account).first()
    return json.dumps(procfile_data.procfile_data_to_json())


@account_request.route("/profile/deviceamount/<account>", methods=['GET'])
def get_every_group_device_amount(account):
    data_count = db.session.query(
        (func.count('listname')-1)).filter(Grouplist_entity.account == account).group_by('listname').all()
    return_list = []
    if data_count is not None:
        for data in data_count:
            return_list.append(data[0])
    return json.dumps(return_list, ensure_ascii=False)


@account_request.route("/profile/profile_image", methods=['POST'])
def save_profile_image():
    json_data = request.get_json()
    account = json_data.get('account')
    profile_image = json_data.get('profile_image')
    AccountEntity.query.filter_by(account=account).update({
        'profile_image': profile_image})
    db.session.commit()
    return json.dumps(SUCCESS, ensure_ascii=False)