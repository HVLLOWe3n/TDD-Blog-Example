from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('new/post/', views.New_Post.as_view(), name='new_mail_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
