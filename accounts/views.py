from django.views.generic import CreateView
from accounts.models import CustomUser

class CustomUserCreateView(CreateView):
    model = CustomUser
    template_name = "register.sing_up.html"
