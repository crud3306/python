# -*- coding: utf-8 -*-
from flask import Blueprint, url_for

__author__ = 'qianm'

web = Blueprint('web', __name__, template_folder='templates')

from app.web import book