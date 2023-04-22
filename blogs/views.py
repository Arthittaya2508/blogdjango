from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogs

# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:2]

    return render (request,"frontend/index.html",{'categories':categories,'blogs':blogs,'latest':latest})

def blogDetail(request,id):
    singleBlog = Blogs.objects.get(id=id)
    singleBlog.View = singleBlog.View+1
    singleBlog.save()
    return render (request,"frontend/blogDetail.html",{"blog":singleBlog})
