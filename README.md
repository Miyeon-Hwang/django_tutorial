# django_tutorial
https://docs.djangoproject.com/ko/4.0/intro/tutorial01/</br>
https://wikidocs.net/70649

### @ django project 관련 커맨드
```
# 커맨드 정리

# Django project를 구성하는 코드를 자동 생성
django-admin startproject directory_name

# Django 서버 실행
py manage.py runserver 8080

# Django project 내 app 자동 생성(Django project directory 에서 실행해야 함)
py manage.py startapp app_directory_name
또는
django-admin startapp app_directory_name

```

### URL과 뷰함수 간의 매핑
  * app 내에서 view.py와 urls.py에 뷰함수와 url 매핑이 필요함
  * 클라이언트 요청이 들어오면 urls.py에서 url 매핑을 확인하고 해당 뷰함수를 호출하게 됨.
  ```
  # project의 urls.py -------------------------------------------------------------------
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      # project 전체의 urls.py 와 각 app의 urls.py 의 분리!
      # "polls/"로 시작하는 페이지를 요청하면 이제 polls/urls.py 파일의 매핑 정보를 읽어서 처리
      path('polls/', include('polls.urls')),
      path('admin/', admin.site.urls),
  ]
  
  # polls/urls.py ------------------------------------------------------------------------
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.index, name='index'),       # name 파라미터 : URL 이름을 설정. 템플릿을 포함한 Django 어디에서나 해당 이름으로 참조할 수 있음.  
  ]
  
  # polls/views.py ------------------------------------------------------------------------
  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Hello, world. You're at the polls index.")
  ```
  
