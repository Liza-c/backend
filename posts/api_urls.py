from posts.api import PostRetrieveAPIView, PostListAPIView

from django.urls import path


app_name = "posts_api"

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name = "posts"),
    path("posts/<int:id>", PostRetrieveAPIView.as_view(), name = "post_detail"),


]

