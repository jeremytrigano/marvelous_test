import os

SECRET_KEY = '"e!E$J&6tWBCZ(b\t87FsO+YG'

FB_APP_ID = 802827976844073

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
