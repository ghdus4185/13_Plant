from django.shortcuts import render,redirect,get_object_or_404
from .models import Write,Comment
from .forms import WriteForm,CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

def index(request):
    writes = Write.objects.all()
    context = {
        'writes': writes
    }
    return render(request,'index.html', context)

@login_required
def create(request):
    if request.method=='POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            writes=form.save(commit=False)
            writes.user = request.user
            writes.cnt = 0
            writes.save()
            return redirect('todos:index')
    else:
        form = WriteForm()
    context={
        'form': form,
    }
    return render(request,'post.html',context)

def detail(request,id):
    write = get_object_or_404(Write, id=id)
    comment_form = CommentForm()
    write.cnt += 1
    write.save()
    context = {
        'write': write,
        'comment_form':comment_form,
    }
    return render(request, 'detail.html', context)

def delete(request,id):
    if request.method=='POST':
        get_object_or_404(Write,id=id).delete()
        return redirect('todos:index')
    else:
        return redirect('todos:index')

def update(request,id):
    write=get_object_or_404(Write,id=id)
    if request.method=='POST':
        form = WriteForm(request.POST, instance=write)
        if form.is_valid():
            form.save()
            
            return redirect('todos:detail',id)

    else:
        form = WriteForm(instance=write)
    context = {
        'form':form,
    }
    return render(request,'post.html', context)

@require_POST
def comment_create(request,id):
    write = get_object_or_404(Write,id=id)
    comments_form = CommentForm(request.POST)
    if comments_form.is_valid():
        comment_ = comments_form.save(commit=False)
        comment_.write = write
        comment_.user = request.user
        comment_.save()
    return redirect('todos:detail',id)

@require_POST
def comment_delete(request,id1,id2):
    get_object_or_404(Comment,id=id2).delete()
    return redirect('todos:detail',id1)

def search(request):
    if request.method == 'POST':
        a = request.POST
        keyword = request.POST.get('keyword')
        writes = Write.objects.filter(title__icontains=keyword)
        context = {
            'writes': writes,
            'a': a
        }
        return render(request, 'search.html', context)
    else:
        write = Write.objects.all()
        context = {
            'writes': writes
        }
        return render(request, 'search.html', context)