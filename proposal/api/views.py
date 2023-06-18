import json

from django.http import JsonResponse

from rest_framework.views import APIView

from proposal.tasks import process_proposal
from proposal.models import ProposalForm, Proposal

class SendProposalApiView(APIView):

  def post(self, request):

    document = request.POST.get('document')
    name = request.POST.get('name')

    result = process_proposal.delay(document, name).get()
    json_result = json.loads(result)

    status = False
    if json_result["approved"]:
      status = ""

    Proposal.objects.create(
      proposal_form=ProposalForm.objects.get(main=True),
      document=document,
      status=status,
      needs_human_approval=json_result["approved"]
    )

    return JsonResponse(json_result)