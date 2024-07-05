from drf_writable_nested import serializers
from resume.models import Resume
from resume.serializers.resume_section_serializer import ResumeSectionSerializer


class ResumeSerializer(serializers.WritableNestedModelSerializer):
    sections = ResumeSectionSerializer(many=True)

    class Meta:
        model = Resume
        exclude = ("is_template", "user", "deleted_at", "deleted_by_cascade")
