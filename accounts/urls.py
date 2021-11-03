from django.contrib import admin
from django.urls import path
from .views import RegisterViewsPost,home,success,register_attempt,login_attempt,error_page,token_send,verify
urlpatterns = [
    
    path('' ,  home  , name="home"),
    path('register/' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('RegisterViewsPost/', RegisterViewsPost.as_view())


    # path('register/', jobregistrationView.as_view()),
    # path('profile/', views.profileView.as_view()),


    
   
]
