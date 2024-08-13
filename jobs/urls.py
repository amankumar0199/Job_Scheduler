from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobView

router = DefaultRouter()
router.register(r'jobs', JobView)

urlpatterns = [
    path('', include(router.urls))
]