from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("<int:question_id>/", views.detail, name="detail"),  # Details page
    path("<int:question_id>/results/", views.results, name="results"),  # Results page
    path("<int:question_id>/vote/", views.vote, name="vote"),  # Voting page
]
