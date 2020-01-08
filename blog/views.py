from django.shortcuts import render
from django.utils import timezone
from .models import NewTestCase
from django.shortcuts import render, get_object_or_404
from .forms import TestCaseForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def new_test_case(request):
    if request.method == "POST":
        form = TestCaseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:       
        form = TestCaseForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)
    if request.method == "POST":
        form = TestCaseForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = TestCaseForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})  
      
def post_delete(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)  
    post.delete()
    posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return redirect('post_list')
    #return render(request, 'blog/post_list.html', {'posts' : posts})

