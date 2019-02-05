from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from . import models
from ppanggram.users import models as user_models

class SmallImageSerializer(serializers.ModelSerializer):

    """ Used for the notifications """

    class Meta:
        model = models.Image
        fields = (
            'file',
        )


class CountImagesSerializer(serializers.ModelSerializer):

    class Meta:
            model = models.Image
            fields = (
                'id',
                'file',
                'comment_count',
                'like_count'
            )

class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):

    # image = ImageSerializer()

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    # likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()


    class Meta:
        model = models.Image
        # fields = '__all__'
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            # 'likes',
            'like_count',
            'creator',
            'tags',
            'created_at'
        )


class LikeSerializer(serializers.ModelSerializer):
    
    # image = ImageSerializer()

    class Meta:
        model = models.Like
        fields = (
            'creator',
        )

class InputImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
        )