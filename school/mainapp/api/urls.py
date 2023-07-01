from django.urls import path, include
from mainapp.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('crud',views.StudentViewSet,basename = 'student')

urlpatterns = [path ('',include(router.urls))]