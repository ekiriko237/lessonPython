#  create '23.xx.xx
#  s.nakamori 
from webL import db
db.create_books_table()

from flask import Flask

app = Flask(__name__)
import webL.main

