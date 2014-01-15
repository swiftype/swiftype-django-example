from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from blog.models import Post
 
def index(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': posts, 'swiftype_engine_key': settings.SWIFTYPE_ENGINE_KEY})
 
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post })
