from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailsView.as_view(), name="details"),
    path('result/<int:pk>', views.ResultsView.as_view(), name="result"),
    path('vote/<int:question_id>', views.vote, name="vote"),
]
