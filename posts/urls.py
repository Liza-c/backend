from django.urls import path
#from posts.api import test_api

from posts.views import (PostCreateView, PostDeleteView, PostDetailView,
                         PostsListView, PostUpdateView)
from django.urls import path, include 
#from posts.api import posts

# We use this for namespaces in urls in templates
app_name = "posts"

urlpatterns = [
    path("", PostsListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("new/", PostCreateView.as_view(), name="create"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
    # API
    #path("posts/", posts, name = "posts"),
]