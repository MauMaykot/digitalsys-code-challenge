from django.urls import path
from .views import SendProposalApiView

urlpatterns = [
  path("send_proposal/", SendProposalApiView.as_view())
]