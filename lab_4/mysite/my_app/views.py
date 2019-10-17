from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.
#def	index(request):
#	return HttpResponse("Hello, World! I'm at the 'my_app' repository")

# def	get_list(request):
# 	my_variable = "WTF???"
# 	return render(request, 'example.html', {'my_variable': my_variable})

def	get_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'example.html', {'posts': posts})

def	post_detail(request, pk):
	Post.objects.get(pk=pk)
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post' : post})
