from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Ticket


class TicketModelForm(BSModalModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

