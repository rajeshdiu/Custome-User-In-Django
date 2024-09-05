
from django.contrib import admin
from django.urls import path

from myProject.views import *


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage,name="homePage"),
    path('addJobPage/', addJobPage,name="addJobPage"),
    path('viewJobPage/', viewJobPage,name="viewJobPage"),
    path('', signinPage,name="signinPage"),
    path('signupPage/', signupPage,name="signupPage"),
    path('logoutPage/', logoutPage,name="logoutPage"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
