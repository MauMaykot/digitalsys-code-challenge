import os

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import ProposalForm

from dotenv import load_dotenv
load_dotenv()

def home(request):
  return redirect('send_proposal')

def send_proposal(request):

  if ProposalForm.objects.all().count() == 0:
    return HttpResponse({"Nenhum formulário de proposta foi criado, favor criar no admin!"})

  proposal = ProposalForm.objects.get(main=True)

  field_types = []
  for field in proposal.fields.all():
    if field.type not in field_types:
      field_types.append(field.type)

  field_types.sort()

  context = {"proposal": proposal, "field_types": field_types, "base_url": os.environ.get('BASE_URL', 'http://localhost:8000')}

  return render(request, 'proposal.html', context)