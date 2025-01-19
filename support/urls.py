from django.urls import path
from .views import manage_requests,update_request
urlpatterns = [
    path('manage_all/',manage_requests),
    path('update_request/<uuid:reference_id>',update_request)
]
