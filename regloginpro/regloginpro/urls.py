from django.contrib import admin
from django.conf.urls import include,url
from regloginapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reg/',views.registration_view),
    url(r'^$',views.login_view),
    url(r'^home/',views.success_view)
]
