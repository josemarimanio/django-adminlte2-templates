from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('layouts/', include('layouts.urls')),

    path('', RedirectView.as_view(pattern_name='layouts:index'), name='index'),
]
