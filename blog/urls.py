from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
]