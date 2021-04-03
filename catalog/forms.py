from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

from .models import BookInstance

# Создание формы гибким способом без преимуществ DJANGO

# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')

#     def clean_renewal_date(self):
#         data = self.cleaned_data["renewal_date"]
        
#         #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
#         if data < datetime.date.today():
#             raise ValidationError( _('Invalid date - renewal in past') )
#         #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError( _('Invalid date - renewal more than 4 weeks ahead') )        

#         # Помните, что всегда надо возвращать "очищенные" данные.
#         return data


# Создание формы с преимуществами DJANGO

class RenewBookForm(ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        #Проверка того, что дата не в прошлом
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Не забывайте всегда возвращать очищенные данные
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = { 'due_back': _('renewal date'), }
        help_texts = { 'due_back': _('Enter a date between now and 4 weeks (default 3).'), } 
