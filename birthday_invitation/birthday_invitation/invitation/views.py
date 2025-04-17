from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from birthday_invitation.invitation.forms import NameForm

invited_guests = [
            "Kriso",
            "Radi",
            "Ivo",
            "Martin",
            "Sissy",
        ]

# Create your views here.


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = NameForm
    success_url = reverse_lazy('invitation')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        if name in invited_guests:
            return super().form_valid(form)
        else:
            form.add_error('name', 'This name is not recognized.')
            return self.form_invalid(form)

class InvitationView(TemplateView):
    template_name = 'invitation.html'
