from os import path

basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' \
        + path.join(basedir, 'flask_blog.db')
# print(SQLALCHMY_DATABASE_URI)
ENV = 'development'
DEBUG = True
TESTING = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = 'not-a-secret' # Fix later setup ENV var if blog goes live