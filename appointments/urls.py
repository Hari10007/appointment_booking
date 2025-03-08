from django.urls import path
from .views import booking_page, AvailableSlotsView, BookAppointmentView, BookedAppointmentsView

urlpatterns = [
    path('', booking_page, name='booking-page'),
    path('available-slots/<str:date>/', AvailableSlotsView.as_view(), name='available-slots'),
    path('book-appointment/', BookAppointmentView.as_view(), name='book-appointment'),
    path('booked-appointments/', BookedAppointmentsView.as_view(), name='booked-appointments'),
]
