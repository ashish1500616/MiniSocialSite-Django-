from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name="about_view"),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name="create_post"),
    url(r'^post/(?P<pk>\d+)/edit/$',
        views.PostrUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',
        views.PostDeleteView.as_view(), name='delete_view'),
    url(r'^drafts/$', views.DraftListView.as_view(), name="draft"),
    url(r'^post/(?P<pk>\d+)/comment/$',
        views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',
        views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',
        views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',
        views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
]
