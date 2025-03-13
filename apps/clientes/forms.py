from .models import Cliente
from django.forms.models import ModelForm
from formset.richtext.widgets import RichTextarea
from django.forms import fields, forms, widgets
from bootstrap_modal_forms.forms import BSModalModelForm


class ClienteForm(forms.Form):
    nome = fields.RegexField(
        r'^[A-z][-A-z ]+$',
        label="Nome",
        error_messages={'invalid': "Use a primeira letra maiuscula. ex: Marcio"},
        help_text="Must start in upper case followed by one or more lowercase characters.",
    )
    tipo = fields.ChoiceField(
        label="Tipo",
        choices=[('CPF', "CPF"), ('CNPJ', "CNPJ")],
        widget=widgets.RadioSelect,
        error_messages={'invalid_choice': "Please select your gender."},
    )
    documento = fields.CharField(
        label="Documento",
        error_messages={'invalid': "A first name must start in upper case."},
        help_text="Must start in upper case followed by one or more lowercase characters.",
    )
    email = fields.EmailField(
        label="E-mail",
        error_messages={'invalid': "isira um email valido."},
    )
    telefone = fields.CharField(
        label="Telefone",
        error_messages={'invalid': "isira um telefone valido."},
    )


class ClienteModelForm(BSModalModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
