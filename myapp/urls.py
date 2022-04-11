from django.urls import re_path
from .views import discipline_list, discipline_detail, discipline_list_published

urlpatterns = [
    re_path(r'^api/$', discipline_list),
    re_path(r'^api/myapp/(?P<pk>[0-9]+)$', discipline_detail),
    re_path(r'^api/myapp/published$', discipline_list_published),
]
