from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm, RegistrationForm
from django.shortcuts import redirect

#Lab6
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import FormView, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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

def	post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form' : form})

def	post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form' : form})

###############LAB_6################
#Регистрация
class RegistrationForm(FormView):
	form_class = RegistrationForm
	success_url = "/login/"
	template_name = "registration.html"

	def form_valid(self, form):
		form.save()
		return super(RegistrationForm, self).form_valid(form)

#Вход в свой аккаунт
class LoginForm(FormView):
	form_class = LoginForm
	success_url = "/profile/"
	template_name = "login.html"

	def form_valid(self, form):
		self.user = form.get_user()
		login(self.request, self.user)
		return super(LoginForm, self).form_valid(form)

#Валидация и вход
@login_required(login_url='/login/')
def user_profile(request):
	return render(request, 'profile.html')

class LogoutForm(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect("/")