from rest_framework import serializers
from . import models
from ppanggram.images import serializers as images_serializers


class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.CountImagesSerializer(many=True, read_only=True)
    post_count = serializers.ReadOnlyField()  
    followers_count = serializers.ReadOnlyField()  
    following_count = serializers.ReadOnlyField() 

    #ReadOnlyField = 이건 수정을 하지 않는다는 의미
    #왜냐면 걍 내 모델의 property 이니까

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images'
        )


class ListUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )
