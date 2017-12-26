from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rabbits_rest.views import RabbitViewSet

router = DefaultRouter()
router.register('rabbits', RabbitViewSet)

urlpatterns = [
    url('^', include(router.urls))
]
