from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from backend.utils import markdown_to_html


class ModelWithSlug(models.Model):

    title = NotImplemented  # text field
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Post(ModelWithSlug):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=500, unique=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    tags = models.ManyToManyField('Tag', related_name='posts')
    hidden = models.BooleanField(default=True)

    @property
    def html(self):
        return markdown_to_html(self.text)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={
            'year': self.created_at.year,
            'month': '%02i' % self.created_at.month,
            'day': '%02i' % self.created_at.day,
            'slug': self.slug,
        })

    def __str__(self):
        return self.title

    @classmethod
    def unhidden(cls):
        return cls.objects.filter(hidden=False)

    class Meta:
        ordering = ['created_at']


class Tag(ModelWithSlug):

    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('posts:post-by-tag-list', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
