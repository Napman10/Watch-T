from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import IssueSerializer
from rest_framework.views import APIView
from .models import Issue
from rest_framework.response import Response


class IssueView(ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        qs = Issue.objects.all()
        return qs
