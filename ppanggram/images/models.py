from django.db import models
from ppanggram.users import models as user_models
# 장고가 어느 모델을 가져와야할지 모르기 때문에 as를 사용함
from django.utils.encoding import python_2_unicode_compatible # 파이썬2와 호환
# Create your models here.

@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# class Meta는 반복을 피하기 위한 참조값

@python_2_unicode_compatible
class Image(TimeStampedModel):

    """ Image Models """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

# 각 값들이 어떤 데이터를 저장하는지 알려주고
# 이미 존재하고 있지 않은 값들이 때문에 null=True는 필요하지 않음

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

@python_2_unicode_compatible
class Comment(TimeStampedModel):

    """ Comment Models """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class Like(TimeStampedModel):

    """ Like Models """

    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return 'User:{} - Image Caption:{}'.format(self.creator.username, self.image.caption
        )
# ForeginKey 는 각 데이터에 새로운 아이디값을 관계정립함

