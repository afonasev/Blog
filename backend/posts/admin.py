from django.contrib import admin

from backend.utils import AdminModelUrlMixin

from . import models


class TagsInline(admin.TabularInline):

    extra = 0
    model = models.Post.tags.through


class PostsInline(admin.TabularInline):

    readonly_fields = ('post', )
    model = models.Tag.posts.through

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Post)
class Post(admin.ModelAdmin, AdminModelUrlMixin):

    date_hierarchy = 'created_at'
    exclude = ('tags', )
    inlines = (TagsInline, )
    list_display = (
        'title', 'author', 'created_at', 'updated_at', 'hidden', 'link',
    )
    list_editable = ('hidden', )
    list_filter = ('hidden', 'tags')


@admin.register(models.Tag)
class Tag(admin.ModelAdmin, AdminModelUrlMixin):

    inlines = (PostsInline, )
    list_display = ('name', 'link')
