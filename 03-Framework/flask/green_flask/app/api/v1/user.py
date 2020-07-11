# -*- coding: utf-8 -*-
from flask import render_template, flash, request
from . import api

from app.libs.helper import test
from app.libs.httper import HTTP
from app.libs.dbpool import SQLHelper

__author__ = 'qianm'


@api.route('/user/search', methods=['GET', 'POST'])
def user_search():
	r = HTTP.get('https://acemongoapi2018inner.alltosun.net/api/v1/user/login')
	print(r)
	print(test(1, 5))

	obj = SQLHelper()
	result = obj.get_list('select * from classes', [])
	print(result)

	return 'user search'

@api.route('/user/detail', methods=['GET', 'POST'])
def user_detail():
	return 'user detail'