from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

from .forms import SignUp, UserUpdateForm, ProfileUpdateForm
from .models import User, ChatMessage


def signup_view(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            login(request, user)
            return redirect("chat_home")
    else:
        form = SignUp()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def chat_home(request):
    # Get all users except the current user
    users = User.objects.exclude(id=request.user.id)
    return render(request, "chat/chat.html", {"users": users})


@login_required
def get_messages(request, user_id):
    """
    Retrieve chat messages between current user and selected user
    """
    messages = ChatMessage.objects.filter(
        (
            Q(sender=request.user, receiver_id=user_id)
            | Q(sender_id=user_id, receiver=request.user)
        )
    ).order_by("timestamp")

    message_list = [
        {
            "content": msg.content,
            "sender_id": msg.sender.id,
            "timestamp": msg.timestamp.isoformat(),
        }
        for msg in messages
    ]

    return JsonResponse(message_list, safe=False)


@login_required
def update_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("chat_home")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(
        request,
        "accounts/profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )

