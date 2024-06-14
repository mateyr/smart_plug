from django.urls import path

from plugs import consumers

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.controls, name="controls"),
    path("off", views.off, name="off"),
    path("on", views.on, name="on"),
    path("emeter_monthly", views.emeter_monthly, name="emeter_monthly"),
]
