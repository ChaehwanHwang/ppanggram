from django.db import models
from ppanggram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# class Meta는 반복을 피하기 위한 참조값

class Image(TimeStampedModel):

    """ Image Models """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

# 각 값들이 어떤 데이터를 저장하는지 알려주고
# 이미 존재하고 있지 않은 값들이 때문에 null=True는 필요하지 않음

class Comment(TimeStampedModel):

    """ Comment Models """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

class Like(TimeStampedModel):

    """ Like Models """

    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)


