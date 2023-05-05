"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaacpqk728r8869c0n0-a.oregon-postgres.render.com",
        database="to_do_list_o7l7",
        user="to_do_list_o7l7_user",
        password="55kI2g35tiaYZz3UmPbDIoUpVXbmlYtM")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
