from django.shortcuts import render

# Create your views here.

def news(request):
    context = {
    }
    return render(request, 'news/news.html', context)

def news_post(request):
    context = {
    }
    return render(request, 'news/news_post.html', context)

def signin(request):
    context = {
    }
    return render(request, 'news/signin.html', context)

def logout(request):
    context = {
    }
    return render(request, 'news/ogout.html', context)
