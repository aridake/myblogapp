from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    #return HttpResponse("Hello, world. this page is posting_page")
    posts = Post.objects.order_by('-published_date') #Postで出来ているデータを降順で並び替えて表示
    return render(request,'posts/index.html',{'posts' : posts}) #index.htmlを呼び出す際にpostsをもった状態で呼び出している

def post_detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'posts/post_detail.html',{'post':post})
# Create your views here.