from resume.views.resume_base_apiview import (
    ResumeListCreateBaseAPIView,
    ResumeRetrieveUpdateDestroyBaseAPIView,
)


class ResumeListCreateAPIView(ResumeListCreateBaseAPIView):
    is_template = False


class ResumeRetrieveUpdateDestroyAPIView(ResumeRetrieveUpdateDestroyBaseAPIView):
    is_template = False
