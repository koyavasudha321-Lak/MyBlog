from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Contact
from django.core.paginator import Paginator
from blog.models import Category,Post,Comment

# Create your views here.
def home(request):

	#return render(request, 'blog/blog.html')
	posts = Post.objects.filter(is_published=False).order_by('posted_at')
	
	posts = Paginator(posts, 1) # Show 25 contacts per page.
	page = request.GET.get('page')
	posts = posts.get_page(page)
	

	context = {
		'posts': posts,
		
	}
	return render(request,'blog/blog.html',context)
		


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		c = Contact(name=name, email=email,subject=subject,message=message)
		c.save()
		return redirect('contact')
	return render(request, 'pages/contact.html')

def about(request):
	return render(request, 'pages/about.html')

def dash(request):
	count = User.objects.count()
	
	context = {
		'count': count,
		}
	return render(request, 'pages/dashboard.html', context)
