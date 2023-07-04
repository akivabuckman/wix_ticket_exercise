from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import generics
import json
import datetime
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]

    # The following line (Line 16) is Exercise 1 instruction. It is commented out to prevent variable redundancy
    # search_fields = ['title']

    # The following line (Line 19) is Exercise 3 instruction
    search_fields = ['title', 'content', 'userEmail']

    # The following line (Lines 22-24) are Exercise 2 instruction
    filterset_fields = {
        'creationTime': ['gte', 'lte'],
    }

    # Populate queryset with data from data.json
    def get_queryset(self):
        with open('ticket_app/data.json', 'r', encoding='utf-8') as f:
            all_ticket_data = json.load(f)

        for ticket_data in all_ticket_data:
            # Convert the given millisecond timestamp into datetime object
            timestamp = ticket_data['creationTime']
            milliseconds = timestamp % 1000
            seconds = timestamp // 1000

            dt = datetime.datetime.fromtimestamp(seconds)
            dt = dt.replace(microsecond=milliseconds * 1000)

            # Create Ticket object instances
            try:
                ticket = Ticket(
                    id=ticket_data['id'],
                    title=ticket_data['title'],
                    content=ticket_data['content'],
                    userEmail=ticket_data['userEmail'],
                    creationTime=dt,
                    labels=ticket_data['labels'],
                )
                ticket.save()
            except KeyError:  # for tickets with no 'label' field
                ticket = Ticket(
                    id=ticket_data['id'],
                    title=ticket_data['title'],
                    content=ticket_data['content'],
                    userEmail=ticket_data['userEmail'],
                    creationTime=dt
                )
                ticket.save()

        queryset = Ticket.objects.all()
        return queryset
