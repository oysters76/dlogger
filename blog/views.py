from django.shortcuts import render 
from .models import Post 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about!'})

class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class DoesUserOwnPostMixim(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        post = self.get_object() 
        return self.request.user == post.author 

class PostUpdateView(LoginRequiredMixin,DoesUserOwnPostMixim, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DoesUserOwnPostMixim, DeleteView):
    model = Post 
    success_url = '/'
    