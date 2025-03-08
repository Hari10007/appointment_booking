from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Appointment
from .serializers import AppointmentSerializer
from datetime import time

AVAILABLE_SLOTS = [
    time(10, 0), time(10, 30), time(11, 0), time(11, 30),
    time(12, 0), time(12, 30),
    time(14, 0), time(14, 30), time(15, 0), time(15, 30),
    time(16, 0), time(16, 30)
]


def booking_page(request):
    return render(request, 'appointments/booking.html')

class AvailableSlotsView(APIView):
    def get(self, request, date):
        booked_slots = Appointment.objects.filter(date=date).values_list('time_slot', flat=True)
        available_slots = [slot for slot in AVAILABLE_SLOTS if slot not in booked_slots]
        formatted_slots = [slot.strftime('%I:%M %p') for slot in available_slots]
        return Response({'available_slots': formatted_slots}, status=status.HTTP_200_OK)

class BookAppointmentView(APIView):
    print("----------------------")
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookedAppointmentsView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all().order_by('date', 'time_slot')
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
