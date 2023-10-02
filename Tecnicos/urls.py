from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import TecnicoView

router = routers.DefaultRouter()
router.register(r'tecnicos', TecnicoView, 'tecnicos')

#app_name='tecnicos'

urlpatterns = [

    path( 'api2/v2/', include(router.urls) ),
    path( 'docs2/', include_docs_urls(title='Tecnicos API') )

]