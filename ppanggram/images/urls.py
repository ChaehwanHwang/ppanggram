from django.conf.urls import url
from . import views

app_name = 'images' #django 2.0이면 추가해야함
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Images.as_view(),
        name='feed'
    ),

    url(
        regex=r'^(?P<image_id>[0-9]+)/$',
        view=views.ImageDetail.as_view(),
        name='image_detail'
    ),

    url(
        regex=r'^(?P<image_id>[0-9]+)/likes/$',
        view=views.LikeImage.as_view(),
        name='like_Image'
    ),

    url(
        regex=r'^(?P<image_id>[0-9]+)/unlikes/$',
        view=views.UnLikeImage.as_view(),
        name='like_Image'
    ),

    url(
        regex=r'^(?P<image_id>[0-9]+)/comments/$',
        view=views.CommentOnImage.as_view(),
        name='comment_Image'
    ),

    url(
        regex=r'^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$',
        view=views.ModerateComments.as_view(),
        name='comment_Image'
    ),

    url(
        regex=r'^comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),

    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    )
]








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

