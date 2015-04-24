from django.shortcuts import render
from trips.models import Post

# Create your views here.
def hello_world(request):
	data = {'curr_time':datetime.now()}
	return render(request, 'hello_world.html', data)

def home(request):
	# get all the posts
	posts = Post.objects.all()
	return render(request, 'home.html', {'posts':posts})