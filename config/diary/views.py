import datetime
from django.shortcuts import render, redirect
from diary.models import Article

# Create your views here.


def list(request):
    start_date = datetime.datetime(2020, 1, 18, 3)
    end_date = datetime.datetime(2020, 1, 18, 9)
    queryset = Article.objects.all().filter(created_at__range=(start_date, end_date))
    return render(request, 'list.html', {'articles': queryset})

def read(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'read.html', {'article': article})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        article = Article.objects.create(title=title, content=content)
        return redirect('articles-read', article.id)

def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'update.html', {'article': article})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        article.title = title
        article.content = content

        article.save()

        return redirect('articles-read', article.id)

def delete(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'GET':
        return redirect('articles-read', article.id)
    elif request.method == 'POST':
        article.delete()
        return redirect('articles-list')