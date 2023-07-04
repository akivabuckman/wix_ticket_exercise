from django.contrib import admin
from django.urls import path, include
from ticket_app.views import TicketListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', TicketListView.as_view(), name='tickets'),
]
