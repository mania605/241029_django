from django.urls import path
from .import views

#순서3 - 브래우저에 들어온 url 요청 패턴을 확인해서 views.py에 있는 함수 호출

#주소창에 localhost:8000/posts 라는 오ㅛ청이 들어오면 아래 url패턴이 인지해서 view 파일에있는 posts함수 실행
urlpatterns = [
  path('posts', views.posts, name='posts')
]