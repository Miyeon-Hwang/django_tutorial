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


# database migration : 모델(즉, 당신의 데이터베이스 스키마)의 변경사항을 디스크에 저장하는 방법
# 프로젝트 내 각 앱이 필요로 하는 데이터베이스 테이블들을 생성하는 명령
python manage.py migrate

# 모델이 신규로 생성되거나 변경되면 makemigrations 명령을 먼저 수행한 후에 migrate 명령을 수행
# makemigrations 뒤에 특정 app name을 붙여도 됨.(해당 app 내 모델에 대해서만 makemigrations 수행
python manage.py makemigrations
python manage.py migrate


# 장고 shell 실행
# 장고에 필요한 환경들이 자동으로 설정되어 실행됨
python manage.py shell   # 종료할 땐 quit()


# 장고 admin 을 위한 user 생성
python manage.py createsuperuser
```
</br>

## URL과 뷰함수 간의 매핑
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
  
## DB Migration
  * settings.py의 INSTALLED_APPS 중에서 DB가 필요한 APP에 대해서 migration 수행
    - app에 model이 추가되면 프로젝트 settings.py 파일의 INSTALLED_APPS 항목에 해당 app 추가해줘야 migration의 대상이 됨.
  * 동작 중인 데이터베이스를 자료 손실 없이 업그레이드 하는 데 최적화 되어 있음
  * **makemigrations**
    - 모델을 생성하거나 모델에 변화가 있을 경우에 실행하는 명령
    - makemigrations을 수행하면 해당 app 디렉토리 migrations에 장고가 테이블 작업을 수행하기 위한 작업 파일(예: 0001_initial.py)을 생성하는 명령
  * **sqlmigrate**
    - makemigrations로 데이터베이스 작업 파일을 생성하고 migrate 명령을 실행하기 전에 실제 어떤 쿼리문이 실행되는지 확인할 수 있음
    
## model query
  * 참고 : https://docs.djangoproject.com/en/4.0/topics/db/queries/
  * filter함수 "__"
    - Use double underscores to separate relationships. This works as many levels deep as you want; there's no limit.
    - https://docs.djangoproject.com/ko/4.0/topics/db/queries/#field-lookups-intro
    - Example
      - Question.objects.filter(question_text__contains='장고')
      - Question.objects.filter(question_text__startswith='What')
      - Choice.objects.filter(question__pub_date__year=current_year)
  * ForeignKey "연결모델명_set"
    - Django creates a set to hold the "other side" of a ForeignKey relation(e.g. a question's choice) which can be accessed via the API.
    - used in a **one-to-many** or **many-to-many** related context
    - https://docs.djangoproject.com/ko/4.0/ref/models/relations/
    - tutorial model을 예로 들면,
      - Choice가 Question을 ForeingnKey로 가짐
      - Question은 여러개의 Choice를 가짐(one-to-many) : choice_set(QuerySet)으로 Question에서 역방향으로 접근 가능
    ```
    q = Question.objects.get(pk=1)
    
    q.choice_set.all()
    q.choice_set.create(choice_text='Not much', votes=0)
    q.choice_set.count()
    ```
    
