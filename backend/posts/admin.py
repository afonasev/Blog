from django.contrib import admin

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
class Post(admin.ModelAdmin):

    date_hierarchy = 'created_at'
    exclude = ('tags', )
    inlines = (TagsInline, )
    list_display = (
        'title', 'author', 'created_at', 'updated_at', 'hidden', 'link',
    )
    list_editable = ('hidden', )
    list_filter = ('hidden', 'tags')

    @staticmethod
    def link(post):
        return f'<a href="{post.get_absolute_url()}">page</a>'
    link.allow_tags = True


@admin.register(models.Tag)
class Tag(admin.ModelAdmin):

    inlines = (PostsInline, )
