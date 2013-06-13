from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    edition = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    posted_by = models.ForeignKey(User, null=True, blank=True)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

    def was_posted_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <  now

	was_posted_recently.admin_order_field = 'pub_date'
    was_posted_recently.boolean = True
    was_posted_recently.short_description = 'Posted recently?'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'publisher', 'edition', 'isbn']