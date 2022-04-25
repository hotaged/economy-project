"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views.static import serve

from quizes import views

admin.site.site_header = "Войти как администратор"
admin.site.site_title = "Тесты по экономике"
admin.site.index_title = "Economy tests"

urlpatterns = [
  path('admin/', admin.site.urls),
  path('home/', views.home),

  path('quiz/<str:uuid>', views.quiz),
  path('accept-quiz', views.accept_quiz),

  path('', RedirectView.as_view(url='home/')),
  path('full/home', views.home_template),
  path('full/rusult', views.result_template),
  path('full/quiz', views.quiz_template),

   re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
   re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_ROOT,
                                                                          document_root=settings.STATIC_ROOT)
