DIALECT = 'mysql'
DRIVER = 'pymysql'
host_name = 'us-cdbr-iron-east-01.cleardb.net'
port = '3306'
database_name = 'heroku_958abfe7827ab0e'
user_name = 'baa493f1d883db'
password = 'ff06ab9f'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}/{}'.format(DIALECT, DRIVER, user_name, password, host_name, database_name)
SQLALCHEMY_TRACK_MODIFICATIONS = False