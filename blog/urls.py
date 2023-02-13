from django.urls import path, include
from . import views

# blog 앱 내부 경로를 지정하는 부분
# urlpatterns = [
#     path('', views.index),# /blog 뒤에 달린 주소가 없음.
#     path('index2/', views.index2)
# ]

urlpatterns = [
    path('', views.PostList.as_view()) # FBV를 생성
]