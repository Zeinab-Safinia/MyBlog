from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog_view(request):
    posts =  Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)
def blog_single(request):
    return render(request, 'blog/blog-single.html')

def post_view(request, pid):
    post = get_object_or_404(Post, id=pid)
    post.counted_view += 1
    post.save()
    return redirect('blog:index')