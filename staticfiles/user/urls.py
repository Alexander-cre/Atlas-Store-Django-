from django.urls import path 
from .views import register_view  , login_view ,logout_view ,profile_update_view , profile_view


app_name = 'user'   #Declaring namespace

urlpatterns = [   
    path('signup/', register_view , name='register_view'),

    path('profile/update/', profile_update_view , name='profile_update'),
    
    path('profile/', profile_view, name='profile'),

    path('login/', login_view , name='login_view '),

    path('logout/', logout_view , name='logout_view '),
]