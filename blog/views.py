from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# posts = [
#     {
#         'author': 'DivyanshuS',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': 'August 13 2019'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second Post Content',
#         'date_posted': 'August 14 2019'
#     }
# ]
