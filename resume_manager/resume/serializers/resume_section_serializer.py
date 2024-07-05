from rest_framework import serializers
from resume.models import ResumeSection


class ResumeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeSection
        fields = "__all__"
