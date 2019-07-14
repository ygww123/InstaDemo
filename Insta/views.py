from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from Insta.forms import CustomUserCreationForm

# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "index.html"
    login_url = 'login'


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ('title',)


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
