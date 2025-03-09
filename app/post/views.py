from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import CommentForm
from .models import Post, Comment


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_details.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "post_text"]
    template_name = 'post/create_post.html'
    success_url = reverse_lazy("post_details")
    context_object_name = "post"

    def form_valid(self, form):
        # Устанавливаем автором поста текущего пользователя
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Возвращаем URL с использованием pk созданного поста
        return reverse("post_details",
                       kwargs={"pk": self.object.pk})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "post_text"]
    template_name = "post/edit_post.html"
    success_url = reverse_lazy("post_details")
    context_object_name = "post"

    def get_success_url(self):
        # Возвращаем URL с использованием pk отредактированного поста
        return reverse("post_details",
                       kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_details", pk=post.id)

    else:
        form = CommentForm()

    return render(request, "post/add_comment.html",
                  {"form": form, "post": post})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        comment.delete()
        return redirect("post_details", pk=comment.post.id)
