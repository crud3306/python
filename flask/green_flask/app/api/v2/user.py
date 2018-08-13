# -*- coding: utf-8 -*-
from flask import render_template, flash, request
from . import api

__author__ = 'qianm'


@api.route('/user/search', methods=['GET', 'POST'])
def user_search():
	return 'user search'

@api.route('/user/detail', methods=['GET', 'POST'])
def user_detail():
	return 'user detail'

@api.before_request
def process_request1(*args, **kwargs):
	print('我api_v2_user来了1')