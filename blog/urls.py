from django.urls import path

from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogDeleteView,
    BlogCreateView,
    BlogCommentView,
)

urlpatterns = [
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('new/', BlogCreateView.as_view(), name='blog_new'),
    path('<int:pk>/comment/', BlogCommentView.as_view(), name='new_comment'),
    path('', BlogListView.as_view(), name='home'),
]
