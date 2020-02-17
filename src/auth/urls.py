from django.urls import path

from . import views

urlpatterns = [
    path(r'signup/', views.signup_view,  name="signup")
]
