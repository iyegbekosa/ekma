from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('old', views.index_old, name='index-old'),
    path('about', views.about, name='about'),
    path('academics', views.academics, name='academics'),
    path('admission', views.admission, name='admission'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/<int:album_id>/', views.album_detail, name='album_detail'),
]
