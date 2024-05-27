from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('myapp.urls')),
    path('', lambda request: HttpResponseRedirect('/search/')),
]


