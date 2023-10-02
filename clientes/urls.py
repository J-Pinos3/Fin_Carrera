from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import ClienteView

router = routers.DefaultRouter()
router.register(r'clientes', ClienteView, 'clientes')

#app_name='clientes'

urlpatterns = [

    path( 'api3/v3/', include(router.urls) ),
    path( 'docs3/', include_docs_urls(title='Clientes API') )

]