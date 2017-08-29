from django.conf.urls import url

from .views import PostDetail, PostList

app_name = 'posts'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post-list'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetail.as_view(), name='post-detail'),
]
