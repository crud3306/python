# -*- coding: utf-8 -*-
from flask import render_template, flash, request
from . import api

__author__ = 'qianm'


@api.route('/book/search', methods=['GET', 'POST'])
def book_search():
	return 'book search'

@api.route('/book/detail', methods=['GET', 'POST'])
def book_detail():
	return 'book detail'