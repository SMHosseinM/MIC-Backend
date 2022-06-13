from django.urls import path
from prayTimes.views import get_all_pray_times, get_specific_pray

urlpatterns = [
    path('', get_all_pray_times, name='pray-schedule'),
    path('<int:pk>', get_specific_pray, name='pray-specific')
]
