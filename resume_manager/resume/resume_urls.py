from django.urls import path
from resume.views import ResumeListCreateAPIView, ResumeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        "",
        ResumeListCreateAPIView.as_view(),
        name="resume_template_list_create",
    ),
    path(
        "<int:pk>/",
        ResumeRetrieveUpdateDestroyAPIView.as_view(),
        name="resume_template_retrieve_update_destroy",
    ),
]
