from django.urls import path
from . import views
from .views import UserLoginView,UserRegistrationView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('members/',  views.MembersListCreate.as_view() , name="members-view"),
    path('members/<int:pk>',  views.MembersRetrieveUpdateDestroy.as_view() , name="members-update"),
]
