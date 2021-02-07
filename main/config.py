SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'db_name': 'test'
})
