from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# class Meta는 반복을 피하기 위한 참조값

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

# 각 값들이 어떤 데이터를 저장하는지 알려주고
# 이미 존재하고 있지 않은 값들이 때문에 null=True는 필요하지 않음

class Comment(TimeStampedModel):

    message = models.TextField()

