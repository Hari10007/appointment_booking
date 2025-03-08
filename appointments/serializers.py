from rest_framework import serializers
from .models import Appointment
from datetime import datetime

class AppointmentSerializer(serializers.ModelSerializer):
    def validate_time_slot(self, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%I:%M %p").time()
            except ValueError:
                raise serializers.ValidationError("Invalid time format. Use 'HH:MM'.")
        return value

    def validate_booked_time_slot(self, value):
        date = self.initial_data.get('date')

        if Appointment.objects.filter(date=date, time_slot=value).exists():
            raise serializers.ValidationError("This time slot is already booked. Please choose another.")

        return value

    class Meta:
        model = Appointment
        fields = "__all__"
