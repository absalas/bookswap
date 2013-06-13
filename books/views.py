# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from books.models import Post, PostForm

def index(request):
    return render(request, 'post/index.html')

def results(request):
	latest_post = Post.objects.all().order_by('-pub_date')[:5]
	context = {'latest_post': latest_post}
	return render(request, 'post/results.html', context)

def profile(request):
	user = request.user
	if request.method == 'POST': # If the form has been submitted...
		form = PostForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			new_post = form.save(commit=False)
			new_post.posted_by = user
			new_post.save()
			return HttpResponseRedirect('')
	else:
		form = PostForm() # An unbound form

	user_posts = Post.objects.filter(posted_by=user)

	return render(request, 'user/profile.html', {
	'form': form, 'user_posts': user_posts,
    })

