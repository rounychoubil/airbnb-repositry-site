from django.views.generic import TemplateView

class HomeViews(TemplateView):
    template_name='home/index.html'

class SalonView(TemplateView):
    template_name='home/salon.html'

class SalleAmangerView(TemplateView):
    template_name='home/sal_amange.html'

class BanhoView(TemplateView):
    template_name='home/banho.html'