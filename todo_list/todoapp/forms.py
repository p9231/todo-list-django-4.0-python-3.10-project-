from django.forms import ModelForm
from todoapp.models import TODO

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields=['title', 'descriptions', 'date_time', 'status_task']