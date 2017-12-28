from django.conf.urls import url, include
from rabbits_rest.views import RabbitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rabbits', RabbitViewSet)

urlpatterns = [
    url('^', include(router.urls))
]
