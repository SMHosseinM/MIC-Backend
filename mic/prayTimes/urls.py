from django.urls import path
from prayTimes.views import get_all_pray, get_pray

urlpatterns = [
    path('', get_all_pray, name='pray-schedule'),
    path('<int:pk>', get_pray, name='pray-specific')
]
