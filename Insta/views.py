from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = "posts.html"

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

# def blog_detail_view(request, primary_key):
#     try:
#         post = Post.objects.get(pk=primary_key)
#     except Post.DoesNotExist:
#         raise Http404('Post does not exist')

#     return render(request, 'post_detail.html', context={'post': posts})
