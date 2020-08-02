from django.urls import path, include
from .views import myform
from rest_framework import routers
from .views import ApprovalsView
from .views import approvereject


router = routers.DefaultRouter()
router.register('MyAPI', ApprovalsView)
urlpatterns = [
	path('form/',myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/',approvereject),
] 
