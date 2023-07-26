from rest_framework import serializers
from apps.posts.models import Category, Movie, Comment, Like, LikeComments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

class LikeCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComments
        fields = "__all__"
    def create(self, validated_data):
        try:
            is_like = LikeComments.objects.get(from_user = validated_data['from_user'], to_comment = validated_data['to_comment'])
            is_like.delete()
            return is_like
        except:
            is_like = LikeComments.objects.create(from_user = validated_data['from_user'], to_comment = validated_data['to_comment'])
            is_like.save()
            return is_like

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
    def create(self, validated_data):
        try:
            is_like = Like.objects.get(from_user = validated_data['from_user'], to_post = validated_data['to_post'])
            is_like.delete()
            return is_like
        except:
            is_like = Like.objects.create(from_user = validated_data['from_user'], to_post = validated_data['to_post'])
            is_like.save()
            return is_like
        
class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    count_likes = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('__all__')
        
    def get_count_likes(self,obj):
        return f'{obj.liked_users.count()}'
    
    def get_count_comments(self,obj):
        return f"{obj.comments.count()}"