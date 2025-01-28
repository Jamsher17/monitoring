
from django.urls import path
from . import views
urlpatterns = [
    path("students",views.StudentListCreate.as_view(), name = 'student-view-create'),
    path("<int:pk>/",view.StudentRetrieveUpdateDestroy.as_view(), name="update")
]