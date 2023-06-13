from django.forms import ModelForm
from django.http import JsonResponse

def _get_errors_from_form(form: ModelForm) -> JsonResponse:
  errors = {}
  for field, errors_list in form.errors.items():
      errors[field] = errors_list[0]
  return JsonResponse({'errors': errors}, status=400)