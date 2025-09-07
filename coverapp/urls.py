from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeViews.as_view(),name="home"),
    path("banho/",views.BanhoView.as_view(),name='banho'),
    path("salamange",views.SalleAmangerView.as_view(),name="sale-manger"),
    path("salon",views.SalonView.as_view(),name='salon'),

]