from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from . import models
from . import form
# Create your views here.
def index(request):
    dataPost = models.Post.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(dataPost,5)
    templateName = 'blog/index.html'
    try:
        dataPost = paginator.page(page)
    except PageNotAnInteger:
        dataPost = paginator.page(1)
    except EmptyPage:
        dataPost = paginator.page(paginator.num_pages)
    content = {
        'title':'Blog',
        'article':'Selamat Datang diBlog, Section blog membahas mengenai Post pada program ini.',
        'data':dataPost,
    }
    return render(request,templateName,content)
def getFormCreate(request):
    templateName = 'blog/form.html'
    formPost = form.FormPost(request.POST or None)
    content = {
        'title':'Form isi',
        'form':formPost,
    }
    if(formPost.is_valid()):
        if(request.method == 'POST'):
            formPost.save()
            return redirect('blog:index')
    return render(request,templateName,content)
def delete(request,inputId):
    models.Post.objects.get(id=inputId).delete()
    return redirect('blog:index')
def updataPost(request,inputId):
    templateName = 'blog/form.html'
    dataPost = models.Post.objects.get(id=inputId)
    data = {
        'title':dataPost.title,
        'author':dataPost.author,
        'article':dataPost.article,
    }
    formPost = form.FormPost(
        request.POST or None,
        initial=data,
        instance=dataPost,
    )
    content = {
        'title':'Form Update',
        'form':formPost
    }
    if (formPost.is_valid()):
        if (request.method == 'POST'):
            formPost.save()
            return redirect('blog:index')
    return render(request,templateName,content)
