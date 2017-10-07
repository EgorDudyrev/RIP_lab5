from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/(?P<id>(\d+))$',views.single_news, name='news'),
    url(r'^users/$',views.UserList.as_view(),name='user_list'),
    url(r'^hotels/$',views.HotelList.as_view(),name='hotel_list'),
    url(r'^bookings/$',views.BookingList.as_view(),name='booking_list'),
    url(r'^$',views.index,name='index')
]
