from django.shortcuts import render
from .models import Post
from django.utils import timezone
import requests

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Inject Query From API (Not related to tutorial)
    api_url = "http://localhost:8080/categories"
    response = requests.get(api_url)
    resp_dict = response.json()

    return render(request, 'blog/post_list.html', {'posts' : posts, 'categories' : resp_dict})


