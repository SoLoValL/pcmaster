from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})
