from django.shortcuts import render,redirect
from .models import Category,Post,Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def blog(request):
	posts = Post.objects.filter(is_published=True).order_by('posted_at')
	categories = Category.objects.all()
	posts = Paginator(posts, 3) # Show 25 contacts per page.
	page = request.GET.get('page')
	posts = posts.get_page(page)
	count = User.objects.count()

	context = {
		'posts': posts,
		'categories':categories,
		'count': count,
	}
	return render(request,'blog/blog.html',context)

def post(request,title):
	#print(title)
	post = Post.objects.get(title=title)
	category = post.category
	
	related_posts = Post.objects.filter(category=category)



	recent_posts = Post.objects.filter(is_published=True).order_by('posted_at')
	categories = Category.objects.all()
	comments = Comment.objects.filter(post=post)
	#print('---' * 10 ,comments)
	context = {
		'related_posts':related_posts,
		'recent_posts':recent_posts,
		'post':post,
		'categories':categories,
		'comments' : comments,

	}

	return render(request, 'blog/post.html',context)



def post_comment(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		comment = request.POST.get('comment')
		website = request.POST.get('website')
		post_id = request.POST.get('id')
		#print('---' * 10, comment, post_id,name)
		post = Post.objects.get(id=post_id)

		c = Comment(name=name, email = email, comment = comment, website = website, post = post)
		c.save()

		return redirect('post',title=post.title)

	return redirect('home')

def search_view(request):
	if request.method == 'GET':
		keyword = request.GET.get('keyword')
		#print('--+--' * 10, keyword)
		#print('==========' * 5,keyword)
		posts = Post.objects.filter(title__icontains=keyword)
		categories = Category.objects.all()
		posts = Paginator(posts, 1) # Show 1 contacts per page.
		page = request.GET.get('page')
		posts = posts.get_page(page)
		#print('---' * 10, posts)
		context = {
			'posts':posts,
			'categories':categories,
		}	
	return render(request,'blog/blog.html', context)

def get_category(request,cat):
	#print('===='*10,cat)
	category = Category.objects.get(name=cat)

	posts = Post.objects.filter(category=category)
	#print('-----' * 10,posts)

	categories = Category.objects.all()
	#print('????----' * 4,categories)
	posts = Paginator(posts, 1) # Show 1 contacts per page.
	page = request.GET.get('page')
	posts = posts.get_page(page)
	


	context = {
		'posts':posts,
		'categories':categories,
		
	}
	return render(request,'blog/blog.html',context)


		

	