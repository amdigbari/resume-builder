from _helpers.permissions import IsOwnerOrReadonly
from django.db import models
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from resume.models import Resume
from resume.serializers import ResumeSerializer


# List/Create API View
class ResumeListCreateBaseAPIView(ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(
            models.Q(is_template=self.is_template)
            & (models.Q(is_public=True) | models.Q(user=self.request.user))
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_template=self.is_template)


# Retrieve/Update/Destroy API View
class ResumeRetrieveUpdateDestroyBaseAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)

    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(
            models.Q(is_template=self.is_template)
            & (models.Q(is_public=True) | models.Q(user=self.request.user))
        )
