from django.urls import path
from .views import new_request,track_request
urlpatterns = [
    path('new_request',new_request),
    path('trace_request/',track_request),
    path('trace_request/<uuid:reference_id>',track_request),
]
