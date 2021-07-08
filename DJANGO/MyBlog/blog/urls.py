from django.urls import path
from blog.views import blog,post


urlpatterns = [
	path('', blog, name='blog'),
	path('post/<str:title>/',post, name='post')

]
	