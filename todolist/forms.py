from django import forms
from . import models

class CreateTask(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTask, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = False

    class Meta:
        model = models.Task
        fields = '__all__'
        exclude = ['user']