from resume.views.resume_base_apiview import (
    ResumeListCreateBaseAPIView,
    ResumeRetrieveUpdateDestroyBaseAPIView,
)


class ResumeTemplateListCreateAPIView(ResumeListCreateBaseAPIView):
    is_template = True


class ResumeTemplateRetrieveUpdateDestroyAPIView(
    ResumeRetrieveUpdateDestroyBaseAPIView
):
    is_template = True
