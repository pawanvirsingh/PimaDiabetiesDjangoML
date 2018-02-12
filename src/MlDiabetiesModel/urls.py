from django.conf.urls import url
import views

urlpatterns = [

 	url(r'^enteryourDetail$', views.DibetiesView.as_view(), name='EnteryourDetail'),

]