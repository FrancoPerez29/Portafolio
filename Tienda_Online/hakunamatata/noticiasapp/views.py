from django.shortcuts import render
from noticiasapp.models import Post

# Create your views here.
def News(request):
    
    posts=Post.objects.all()
    return render(request,"noticias/news.html",{"posts": posts})