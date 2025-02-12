from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer
from .utils import generate_report_file
from .ai_service import generate_ai_remarks

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        report_data = request.data
        report = Report.objects.create(**report_data)

        # Generate AI-based remarks
        report.remarks = generate_ai_remarks(report)
        report.save()

        # Generate report document
        file_url = generate_report_file(report)

        return Response({"message": "Report created", "file_url": file_url})
