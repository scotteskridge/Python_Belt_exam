from django.conf.urls import url, include

from . import views

urlpatterns = [

    url(r'^$', views.index, name = "index"),
    url(r'^next_page$', views.next_page, name = "next_page"),


]
