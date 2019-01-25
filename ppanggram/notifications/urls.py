from django.conf.urls import url
from . import views

app_name = 'notifications' #django 2.0이면 추가해야함
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Notifications.as_view(),
        name='notifications'
    ),
]
