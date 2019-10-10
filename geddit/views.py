from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'geddit/post_list.html', {'posts': posts})

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
            for subgeddit_id in request.POST.getlist('subgeddits'):
                SubGedditPost.objects.create(subgeddit_id=subgeddit_id, post=post)
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'geddit/post_edit.html', {'form': form, 'is_create': True})