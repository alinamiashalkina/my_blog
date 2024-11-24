from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    delete_comment,
)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete_comment'),
]
