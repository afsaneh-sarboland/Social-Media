from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('posts', views.PostList.as_view(), name='posts'),
    path('detail-post/<slug:slug>', views.post_detail, name='PostDetail'),
    path('new-post', views.new_post, name='new_post'),
    path('last-week-posts', views.last_week_posts, name='last_week_posts'),
]
