from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from pages.views import ProjectList, ProjectDetail

urlpatterns = [
    path('',ProjectList.as_view(), name='home'),
    path('project/<int:pk>', ProjectDetail.as_view(),name='project_detail')
]

