from django.contrib import admin
from books.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['publisher']}),
        (None,               {'fields': ['edition']}),
        (None,               {'fields': ['isbn']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'author', 'publisher', 'edition', 'isbn', 'pub_date', 'was_posted_recently')
    list_filter = ['pub_date']
    search_fields = ['title', 'author', 'publisher', 'edition', 'isbn', 'pub_date']
    date_hierarchy = 'pub_date'

admin.site.register(Post, PostAdmin)