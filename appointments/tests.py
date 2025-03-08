from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Appointment
from datetime import date, time, timedelta

class AppointmentTests(TestCase):

    def test_create_appointment(self):
        """Test successful appointment creation."""
        appointment = Appointment.objects.create(
            name='Riafy User', phone_number='1234567890', date=date.today(), time_slot=time(10, 0)
        )
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.name, 'Riafy User')

