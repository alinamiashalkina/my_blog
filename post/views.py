from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, CommentForm
from .models import Post, Comment


@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/post_list.html",
                  {"posts": posts})


@login_required
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post/post_details.html",
                  {"post": post})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # Создаем объект, но пока не сохраняем в базе данных
            post = form.save(commit=False)
            # Добавляем текущего пользователя в качестве автора
            post.author = request.user
            # Сохраняем объект в базе данных
            post.save()
            return redirect("post_details", pk=post.pk)
    else:
        form = PostForm()

    return render(request, "post/create_post.html",
                  {"form": form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # Сохраняем изменения в посте
            return redirect("post_details", pk=post.pk)
    else:
        # Заполняем форму данными существующего поста
        form = PostForm(instance=post)

    return render(request, "post/edit_post.html",
                  {"form": form, "post": post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")


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

