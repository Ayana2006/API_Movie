from rest_framework import generics, viewsets
from apps.posts.models import Movie, Category, Comment, Like, LikeComments
from apps.posts.serializers import MovieSerializer, CategorySerializer, CommentSerializer, LikeSerializer, LikeCommentsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MovieViewSet(viewsets.ModelViewSet): 
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
class LikeCommentsViewSet(viewsets.ModelViewSet):
    queryset = LikeComments.objects.all()
    serializer_class = LikeCommentsSerializer