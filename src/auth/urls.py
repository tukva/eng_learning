from django.urls import path

from auth.views import signup_view, activate, activation_sent_view

urlpatterns = [
    path(r'signup/', signup_view,  name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]
