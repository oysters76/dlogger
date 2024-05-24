from django.shortcuts import render 

posts = [
    {
        'author': 'CoreyMs', 
        'title': 'blog post 1', 
        'content': 'first content post', 
        'date_posted': 'August 26, 2029'
    },
     {
        'author': 'Jane done', 
        'title': 'blog post 2', 
        'content': 'second content post', 
        'date_posted': 'August 27, 2029'
    },
     {
        'author': 'Broseft', 
        'title': 'blog post 3', 
        'content': 'third content post', 
        'date_posted': 'August 28, 2029'
    }
]

# Create your views here.
def home(request):
    context = {'posts': posts, 'title':'Home!'}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about!'})