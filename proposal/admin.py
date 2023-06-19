from django.contrib import admin

from .models import Choice, Field, ProposalForm, Proposal

from django import forms

admin.site.register(Choice)
admin.site.register(Field)

class ProposalFormForm(forms.ModelForm):

  class Meta:
    model = ProposalForm
    fields = '__all__'

  def clean_main(self):
    main = self.cleaned_data["main"]

    if main:
      forms = ProposalForm.objects.all()
      for form in forms:
        form.main = False
        form.save()

    return self.cleaned_data["main"]

class ProposalModelAdmin(admin.ModelAdmin):
  form = ProposalFormForm

admin.site.register(ProposalForm, ProposalModelAdmin)

class ProposalsForm(forms.ModelForm):

  class Meta:
    model = Proposal
    fields = '__all__'

class ProposalModelAdmin(admin.ModelAdmin):
  form = ProposalsForm
  readonly_fields = ["needs_human_approval",]
  list_filter = ["status"]

admin.site.register(Proposal, ProposalModelAdmin)