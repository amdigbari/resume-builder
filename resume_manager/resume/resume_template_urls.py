from django.urls import path
from resume.views import (
    ResumeTemplateListCreateAPIView,
    ResumeTemplateRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "",
        ResumeTemplateListCreateAPIView.as_view(),
        name="resume_template_list_create",
    ),
    path(
        "<int:pk>/",
        ResumeTemplateRetrieveUpdateDestroyAPIView.as_view(),
        name="resume_template_retrieve_update_destroy",
    ),
]
