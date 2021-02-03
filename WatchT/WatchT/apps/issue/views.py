from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import IssueSerializer
from rest_framework.views import APIView
from .models import Issue
from rest_framework.response import Response


class IssueListView(ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class IssueOpenView(RetrieveUpdateAPIView):
    serializer_class = IssueSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Issue.objects.all()


class IssueCreateView(CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    action_map = {
        'post': 'create'
    }
