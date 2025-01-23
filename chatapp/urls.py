from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app import views
from app.consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Authentication
    path("signup/", views.signup_view, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    # Chat
    path("", views.chat_home, name="chat_home"),
    path("profile/", views.update_profile, name="profile"),
    path("chat/messages/<int:user_id>/", views.get_messages, name="get_messages"),
]

