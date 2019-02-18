from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

#단순히 new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')


#입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    myblog = Blog()
    myblog.title = request.GET['title']
    myblog.body = request.GET['body']
    myblog.pub_date = timezone.datetime.now()
    myblog.save()
    return redirect('/myblog/'+str(myblog.id))

