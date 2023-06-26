from django.urls import path
from . import views
urlpatterns = [
    path('',views.DegreeListView.as_view(),name="home"),
    path('programs/',views.ProgramsView.as_view(),name="programs"),
    path('university/',views.UniversityView.as_view(),name="university")
]

