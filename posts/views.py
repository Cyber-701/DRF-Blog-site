from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(generic.ListView):
    """Barcha postlarni ko'rish uchun view."""
    
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    paginate_by = 10


class PostDetailView(generic.DetailView):
    """Postning batafsil ko'rinishi."""
    
    model = Post
    template_name = "detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    """Yangi post yaratish."""
    
    model = Post
    template_name = "create.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("posts:home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """Postni tahrirlash."""
    
    model = Post
    template_name = "update.html"
    context_object_name = "post"
    fields = ["title", "body"]
    success_url = reverse_lazy("posts:home")

    def test_func(self) -> bool:
        """Faqat muallif o'z postini tahrirlashi mumkin."""
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """Postni o'chirish."""
    
    model = Post
    template_name = "delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")

    def test_func(self) -> bool:
        """Faqat muallif o'z postini o'chirishi mumkin."""
        post = self.get_object()
        return post.author == self.request.user
