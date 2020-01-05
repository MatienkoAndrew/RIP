from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.utils import timezone
from .forms import *
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

def main(request):
	query_list = Service.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	paginator = Paginator(query_list, 2)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	return render(request, 'blog/main.html', {'posts': queryset})
	# posts = Service.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# return render(request, 'blog/main.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Service, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.worker = request.user
			post.published_date = timezone.now()
			post.image = form.cleaned_data['image']
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Service, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.worker = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def edit_profile(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = EditProfileForm(instance=request.user)
	return render(request, 'blog/edit_profile.html', {'form':form})

#Регистрация
class RegistrationForm(FormView):
	form_class = RegistrationForm
	success_url = "/login/"
	template_name = "blog/registration.html"

	def form_valid(self, form):
		form.save()
		return super(RegistrationForm, self).form_valid(form)

#Вход в свой аккаунт
class LoginForm(FormView):
	form_class = LoginForm
	success_url = "/profile/"
	template_name = "blog/login.html"

	def form_valid(self, form):
		self.user = form.get_user()
		login(self.request, self.user)
		return super(LoginForm, self).form_valid(form)

#Валидация и вход
@login_required(login_url='/login/')
def user_profile(request):
	return render(request, 'blog/profile.html')

class LogoutForm(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect("/")

