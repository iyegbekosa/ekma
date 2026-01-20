from django.shortcuts import render
from .models import Album, Gallery
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    context = {
        'title':'Home'
    }
    return render(request, 'core/index.html', context)

def index_old(request):
    context = {
        'title':'Old Home'
    }
    return render(request, 'core/index_old.html', context)


def about(request):
    context = {
        'title':'About Us'
    }
    return render(request, 'core/about.html', context)

def academics(request):
    context = {
        'title':'Academics'
    }
    return render(request, 'core/academics.html', context)

def admission(request):
    context = {
        'title':'Admissions'
    }
    return render(request, 'core/admission.html', context)

def contact(request):
    context = {
        'title':'Contact'
    }
    return render(request, 'core/contact.html', context)

def gallery(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
        'title':'Gallery'
    }
    return render(request, 'core/gallery.html', context)

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    images = album.images.all()
    context = {
        'album': album,
        'images': images,
    }
    return render(request, 'core/album_detail.html', context)
