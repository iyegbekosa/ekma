from django.urls import path
from . import views

urlpatterns = [
    path('news', views.news, name='news'),
    path('news_post', views.news_post, name='news_post'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
