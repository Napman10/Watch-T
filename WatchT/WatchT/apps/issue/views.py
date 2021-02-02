from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import IssueSerializer
from rest_framework.views import APIView
from .models import Issue
from rest_framework.response import Response


class IssueView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'issue/issue_test.html'

    def get_queryset(self):
        return Issue.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = IssueSerializer
        return Response({'issues': self.get_queryset(), 'serializer': serializer})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

