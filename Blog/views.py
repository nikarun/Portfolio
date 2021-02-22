from django.shortcuts import render,get_object_or_404
from .models import *
def AllBlogs(request):
    blogs=Blog.objects.all();
    return render(request, 'blog.html',{'blogs':blogs});

def Blogs(request,blog_id):
    blog=get_object_or_404(Blog,pk = blog_id)
    print(blog);
    return render(request, 'blog_bid.html',{'blog':blog});
  
