from django.conf.urls import url

from .views import PostByTagList, PostDetail, PostList

app_name = 'posts'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post-list'),

    url(
        r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/'
        r'(?P<slug>[-\w]*)/$',
        PostDetail.as_view(),
        name='post-detail',
    ),

    url(
        r'^tag/(?P<slug>[\w\s-]+)/$',
        PostByTagList.as_view(),
        name='post-by-tag-list',
    ),
]
