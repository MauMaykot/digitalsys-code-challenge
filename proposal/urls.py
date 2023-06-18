from django.urls import path
from .views import home, send_proposal

urlpatterns = [
  path("", home, name="home"),
  path("send_proposal/", send_proposal, name="send_proposal")
]