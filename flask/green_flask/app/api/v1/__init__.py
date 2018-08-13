# -*- coding: utf-8 -*-
from flask import Blueprint, url_for

__author__ = 'qianm'

api = Blueprint('api_v1', __name__)

@api.before_request
def process_request1(*args, **kwargs):
	print('我api_user来了1')

from app.api.v1 import user, book