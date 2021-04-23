from django.urls import path

from adminPanel.views import AdminProjectCreate, AdminProjectList, AdminProjectUpdate, AdminProjectDelete

urlpatterns = [
    path('create/', AdminProjectCreate.as_view(), name='project_create'),
    path('', AdminProjectList.as_view(), name='project_list'),
    path('update/<int:pk>', AdminProjectUpdate.as_view(),name='project_update'),
    path('delete/<int:pk>', AdminProjectDelete.as_view(),name='projects_delete'),

]
