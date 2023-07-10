from django.urls import path
from . import views

urlpatterns = [ 
    path('signup/', views.signup, name="signup"), # signup
    path('signin/', views.signin, name="signin"), # login
    path('logout/', views.signout, name='logout'), # logout
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todo/', include('todo_app.urls')),
    path('accounts/', include('accounts.urls')), # accounts 추가
    path('admin/', admin.site.urls),
]