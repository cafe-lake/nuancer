from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.search import views

urlpatterns = [
    path(
        "search/",
        views.Search.as_view(),
        name="search",
    )
]