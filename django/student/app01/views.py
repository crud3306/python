from django.shortcuts import render
import pymysql

def classes(request):
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='student', charset='utf8')
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
	conn.execute("select id,title from class")
	class_list = cursor.fetchall()
	cursor.close()
	conn.close()

	return render('classes.html', { 'class_list':class_list })