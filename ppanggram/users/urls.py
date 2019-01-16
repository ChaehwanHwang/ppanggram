from django.conf.urls import url
from . import views

app_name = 'users' #django 2.0이면 추가해야함
urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),

    url(
        regex=r'(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),

    url(
        regex=r'(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='follow_user'
    ),
]