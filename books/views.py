# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from books.models import Post

def index(request):
    return render(request, 'post/index.html')

def results(request):
	latest_post = Post.objects.all().order_by('-pub_date')[:5]
	context = {'latest_post': latest_post}
	return render(request, 'post/results.html', context)