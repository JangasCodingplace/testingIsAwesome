from django.urls import path
from . import views


urlpatterns = [
    path(
        'create/',
        views.CreateCourseAPI.as_view(),
        name="CreateCourseAPI"
    ),
]
