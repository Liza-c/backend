from django.db.models import fields
from django.http import JsonResponse
from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"