from django.urls import path, include
from . import views

urlpatterns = [
    # Auth of users and admins
    path("users/register/", views.CreateUserView.as_view(), name = "register_user"),    
    path("token/", views.TokenObtainPairView.as_view(), name = "get_token"),
    path("token/refresh/", views.TokenRefreshView.as_view(), name = "refresh_token"),

    path("intents/<int:pk>/", views.RetrieveIntentView.as_view(), name = "retrieve_intent"),
    path("intents/<int:pk>/update/", views.UpdateIntentView.as_view(), name = "update_intent"),
    path("intents/<int:pk>/delete/", views.DeleteIntentView.as_view(), name = "delete_intent"),
    path("intents/register/", views.CreateIntentView.as_view(), name = "register_intent"),
    path("intents/", views.ListCreateIntentView.as_view(), name = "list_intent"),

    path("patterns/<int:pk>/", views.RetrievePatternView.as_view(), name = "retrieve_pattern"),
    path("patterns/<int:pk>/update/", views.UpdatePatternView.as_view(), name = "update_pattern"),
    path("patterns/<int:pk>/delete/", views.DeletePatternView.as_view(), name = "delete_pattern"),
    path("patterns/register/", views.CreatePatternView.as_view(), name = "register_pattern"),
    path("patterns/", views.ListCreatePatternView.as_view(), name = "list_pattern"),
    
    path("answers/<int:pk>/", views.RetrieveAnswerView.as_view(), name = "retrieve_answer"),
    path("answers/<int:pk>/update/", views.UpdateAnswerView.as_view(), name = "update_answer"),
    path("answers/<int:pk>/delete/", views.DeleteAnswerView.as_view(), name = "delete_answer"),
    path("answers/register/", views.CreateAnswerView.as_view(), name = "register_answer"),
    path("answers/", views.ListCreateAnswerView.as_view(), name = "list_answer"),
]
