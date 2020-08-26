from django.urls import path
from . import views


urlpatterns = [
    path(
        'registion/',
        views.UserRegistrationAPI.as_view(),
        name="UserRegistrationAPI"
    ),
]
