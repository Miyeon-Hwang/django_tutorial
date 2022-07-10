from django.contrib import admin
from .models import Question


# Question 모델에 세부 기능을 추가할 수 있는 QuestionAdmin 클래스
# 추가할 수 있는 기능들 : https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text'] # 검색 기능 추가


admin.site.register(Question, QuestionAdmin)   # 관리자 화면에서 Question 모델을 관리하도록 등록
