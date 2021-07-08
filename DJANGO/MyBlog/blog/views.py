from django.shortcuts import render,redirect
from .models import Category,Post

# Create your views here.
def blog(request):
	posts = Post.objects.filter(is_published=True)
	categories = Category.objects.all()

	context = {
		'posts' : posts,
		'categories':categories,

	}
	return render(request,'blog/blog.html',context)

def post(request,title):
	#print(title)
	post = Post.objects.get(title=title)
	categories = Category.objects.all()
	context = {
		'post':post,
		'categories':categories,

	}

	return render(request, 'blog/post.html',context)