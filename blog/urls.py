from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='post_list'),
    path('new/post/', views.New_Post.as_view(), name='new_mail_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
