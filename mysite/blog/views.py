from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.filter(status='published')

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'blogs/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status='published',
        created__year=year,
        created__month=month,
        created__day=day,
    )
    return render(request, 'blogs/post_detail.html', {'post': post})