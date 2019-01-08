from django.conf.urls import url
from . import views

app_name = 'images' #django 2.0이면 추가해야함
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),


    # 테스트

    # url(
    #     regex=r'^comments/$',
    #     view=views.ListAllComments.as_view(),
    #     name='all_images'
    # ),
    # url(
    #     regex=r'^likes/$',
    #     view=views.ListAllLikes.as_view(),
    #     name='all_images'
    # )
]
