from django.forms import ModelForm
from .models import Diabeties
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


# class DiabetiesForm(forms.ModelForm):

#   class meta:

#       model=Diabeties
#       fields = '__all__'

class DiabetiesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiabetiesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('preg'),
            Field('plas'),
            Field('pres'),
            Field('skin'),
            Field('test'),
            Field('mass'),
            Field('pedi'),
            Field('age'),
            Submit('update', 'Update', css_class="btn-success"),
            )
    class Meta:
        model = Diabeties
        fields = "__all__"