# -*- coding: utf-8 -*-
from flask import render_template, flash, request
from . import web

__author__ = '七月'


@web.route('/book/search', methods=['GET', 'POST'])
def search():
	return 'book search'

@web.route('/book/detail', methods=['GET', 'POST'])
def detail():
	return 'book detail'

@web.before_request
def process_request1(*args, **kwargs):
	print('我web来了1')