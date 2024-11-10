from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:pk>/', views.delete_comment,
         name='delete_comment'),
]
