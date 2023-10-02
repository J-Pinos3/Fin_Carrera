from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import TicketView

router = routers.DefaultRouter()
router.register(r'tickets', TicketView, 'tickets')

#app_name='tickets'

urlpatterns = [

    path( 'api1/v1/', include(router.urls) ),
    path( 'docs/', include_docs_urls(title='Tickets API') )

]