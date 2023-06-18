import requests

from celery import shared_task

@shared_task(bind=True)
def process_proposal(self, document, name):

  url  = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
  data = {
    "document": document,
    "name": name
  }

  request  = requests.post(url, data)
  response = request.text

  return response