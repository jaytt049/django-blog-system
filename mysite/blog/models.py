from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published')
)



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        default='draft'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    def get_absolute_url(self):
        return reverse('post_detail', args=[
            self.created.year,
            self.created.month,
            self.created.day,
            self.slug
        ])
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title