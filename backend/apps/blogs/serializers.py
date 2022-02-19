from django.contrib.auth.models import User, Group
from apps.blogs.models import Post, PostLike, PostComment, CommentLike
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']


class PostLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostLike
        fields = ['author', 'post']


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostComment
        fields = ['author', 'post', 'content']


class CommentLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['author', 'comment']
