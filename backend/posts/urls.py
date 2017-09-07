from django.conf.urls import url

from .views import PostByTagList, PostDetail, PostList

app_name = 'posts'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post-list'),

    url(
        r'^post/(?P<pk>[0-9]+)/$',
        PostDetail.as_view(),
        name='post-detail',
    ),

    url(
        r'^tag/(?P<name>[\w\s-]+)/$',
        PostByTagList.as_view(),
        name='post-by-tag-list',
    ),
]
