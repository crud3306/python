# -*- coding: utf-8 -*-
from flask import Blueprint, url_for

__author__ = 'qianm'

api = Blueprint('api_v2', __name__)

from app.api.v2 import user