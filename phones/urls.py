from django.urls import path
from .views import PhoneViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('phones', PhoneViewSet, basename='news')

urlpatterns = router.urls



