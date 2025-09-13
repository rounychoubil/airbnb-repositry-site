from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import LocationForm

# frontend section page
class HomeViews(TemplateView):
    template_name='home/index.html'

class SalonView(TemplateView):
    template_name='home/salon.html'

class SalleAmangerView(TemplateView):
    template_name='home/sal_amange.html'

class BanhoView(TemplateView):
    template_name='home/banho.html'

# backen section page

class LocationCreateView(CreateView):
    form_class = LocationForm
    template_name = "home/location.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Accès direct via form.cleaned_data
        date1 = form.cleaned_data['date_in'] 
        date2 = form.cleaned_data['date_out']
        
        # Modifier l'instance de l'objet avant la sauvegarde
        form.instance.customer = self.request.user
        form.instance.price = (date2-date1).days*125
        form.instance.is_avalable = False
        
        # Enregistrer l'objet et continuer la chaîne de méthodes
        return super().form_valid(form)

