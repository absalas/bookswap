# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from books.models import Post

class IndexView(generic.ListView):
    template_name = 'post/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'