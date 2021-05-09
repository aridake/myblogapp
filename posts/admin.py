from django.contrib import admin

'''
Register your models here.
'''

#同ディレクトリのmodels.pyに追加したクラスを読み込む(→読み込んだクラスの関数がサイト上に出てくる)
from .models import Post

#admin.py_add Post_Class
admin.site.register(Post)