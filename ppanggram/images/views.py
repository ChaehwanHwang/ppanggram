#from django.shortcuts import render #우리가 쳄플릿을 사용하고 싶을때 render사용
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models # 모델에서 이미지 오브젝트 가져오기
from . import serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        for following_users in following_users:

            print(following_users.images.all()[:2])

        return Response(data=serializer.data) 




# 이건 테스트 임

# class ListAllImages(APIView):

#     def get(self, request, format=None):

#         all_images = models.Image.objects.all()

#         #파이썬은 브라우저를 모름 그래서 시리얼라이즈를 해야함 (제이슨으로 번역)
#         serializer = serializers.ImageSerializer(all_images, many=True)

#         return Response(data=serializer.data) # response = 기능을 끝낼때 (마지막 문장)


# class ListAllComments(APIView):
    
#     def get(self, request, format=None):

#         all_comments = models.Comment.objects.all()

#         serializer = serializers.CommentSerializer(all_comments, many=True)

#         return Response(data=serializer.data) 


# class ListAllLikes(APIView):
    
#     def get(self, request, format=None):

#         all_likes = models.Like.objects.all()

#         serializer = serializers.LikeSerializer(all_likes, many=True)

#         return Response(data=serializer.data)       