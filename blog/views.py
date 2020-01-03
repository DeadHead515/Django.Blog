from django.shortcuts import render
from .models import Post
#no longer need this import. from django.http import HttpResponse


#creating are posts. post will be equal to a list of dictionaries.

# Create your views here.
def home(request):
#passing our posts context into our homepage by creating dictionary to store it in called context.
#key is posts and the data past in instored in posts as well. 
    context= {
        'posts': Post.objects.all()
}
    return render(request, 'blog/home.html', context )

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})