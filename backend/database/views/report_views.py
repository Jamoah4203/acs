from rest_framework import viewsets
from database.models import Report
from database.serializers import ReportSerializer  

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer  