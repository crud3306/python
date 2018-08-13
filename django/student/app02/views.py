from django.shortcuts import render

# Create your views here.

def classes(request):
	import pymysql

	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='student', charset='utf8')
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
	cursor.execute("select id,title from classes")
	class_list = cursor.fetchall()
	cursor.close()
	conn.close()

	return render(request, 'classes.html', { 'class_list':class_list })


def add_class(request):
	return render(request, 'add_class.html')