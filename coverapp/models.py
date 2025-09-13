from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Location(models.Model):
    customer = models.ForeignKey(CustomUser, verbose_name=_(""), on_delete=models.CASCADE)
    date_in = models.DateField(_("Date in "), auto_now=False, auto_now_add=False)
    date_out = models.DateField(_(" Date out "), auto_now=False, auto_now_add=False)
    price = models.IntegerField(_("Rent price "),default=0)
    is_avalable = models.BooleanField(_("Avalable"),default=True)

    

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

   

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})
