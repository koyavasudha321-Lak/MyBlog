from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'blog/blog.html')

def contact(request):
	return render(request, 'pages/contact.html')

def about(request):
	return render(request, 'pages/about.html')
