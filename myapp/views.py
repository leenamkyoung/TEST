from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects # 쿼리셋 # 메소드     
    return render(request, 'home.html', {'projects': projects})

# 쿼리셋 메소드의 형식
# 모델. 쿼리셋(objects).메소드
