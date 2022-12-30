
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('doc', views.doctor_home, name='doc'),
    path('nurse', views.nurse_home, name='nurse'),
    path('accounts/', include('accounts.urls')),
    path('details/', include('details.urls')),
    path('detail/', include('detail.urls')),
]

