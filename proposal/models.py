from django.db import models

TYPE = [
  ('text', 'Texto curto'),
  ('textarea', 'Texto longo'),
  ('email', 'E-mail'),
  ('checkbox', 'Checkbox'),
  ('select', 'Lista'),
  ('radio', 'Seleção única'),
]

class Choice(models.Model):
  text = models.CharField(max_length=255)

  def __str__(self):
    return self.text

class Field(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255, choices=TYPE)
  choices = models.ManyToManyField(Choice, blank=True)

  def __str__(self):
    return self.name + " (" + self.type + ")"

class ProposalForm(models.Model):
  name   = models.CharField(max_length=255, unique=True)
  fields = models.ManyToManyField(Field, blank=True)
  main   = models.BooleanField(default=False)

  def __str__(self):
    main_text = "Secondary"
    if self.main:
      main_text = "Main"
    return self.name + " (" + main_text + ")"

STATUS = [
  ('', 'Avaliação necessária'),
  ('True', 'Aprovada'),
  ('False', 'Negada'),
]

class Proposal(models.Model):
  proposal_form = models.ForeignKey(ProposalForm, on_delete=models.CASCADE)
  document = models.JSONField()
  status = models.CharField(max_length=255, choices=STATUS, blank=True, null=True)

  needs_human_approval = models.BooleanField(default=False)

  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)

  def __str__(self):

    status = ""
    if self.status == "True":
      status = "Aprovada"
    elif self.status == "False":
      status = "Negada"

    if self.needs_human_approval and self.status == "":
      return "Avaliação humana necessária!"
    elif self.needs_human_approval and self.status != "":
      return "Avaliação humana realizada - " + status
    else:
      return "Negada automaticamente"

  def save(self, *args, **kwargs):
    if not self.needs_human_approval:
      self.status = "False"
    super(Proposal, self).save(*args, **kwargs)