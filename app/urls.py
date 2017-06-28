from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name="about_view"),
    url(r'^$', views.PostListView.as_view(), name='about'),
    url(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view, name="create_post"),
    url(r'^post/(?P<pk>\d+)/edit/$',
        views.PostrUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',
        views.PostDeleteView.as_view(), name='delete_view'),
    url(r'^drafts/$',views.DraftListView.as_view(),name="draft")
]
