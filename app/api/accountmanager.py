from flask import Blueprint
import hashlib, json, re
from flask import request
from app import database
from app.account_entity import AccountEntity

account_request = Blueprint('account_request', __name__)

ACCOUNT_IS_NOT_EXIST = 'account is not exist'
ACCOUNT_ALREADY_EXIST = 'account already exist'
ACCOUNT_TYPE_IS_NOT_ALLOW = 'account type is not an allowed specifications'
SUCCESS = 'success'


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
            return ACCOUNT_IS_NOT_EXIST
        return SUCCESS


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
        return_message = SUCCESS
        account_entity = AccountEntity(account=account, password=sha256_password, name=name, profile_image=profile_image)
        database.add_data(account_entity)
    else:
        return_message = ACCOUNT_ALREADY_EXIST

    return json.dumps(return_message, ensure_ascii=False)


@account_request.route("/procfile/<account>", methods=['GET'])
def get_procfile_data(account):
    procfile_data = AccountEntity.query(AccountEntity).filter(AccountEntity.account == account)
    print(procfile_data)


    return account
