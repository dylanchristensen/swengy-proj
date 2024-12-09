from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from .models import User, Path
from .forms import MyUserCreationForm


# Home Page View
def main_content_view(request):
    return render(request, 'home.html')  # Landing page


# View Path Details
def view_path_view(request):
    path_id = request.GET.get('path_id')  # Fetch the path ID from query parameters

    if path_id:
        # Store the selected path in the session
        request.session['selected_path_id'] = path_id

    # Retrieve the selected path from the session
    selected_path_id = request.session.get('selected_path_id')

    if selected_path_id:
        # Fetch the path if it exists
        path = get_object_or_404(Path, id=selected_path_id)
        return render(request, 'view_path.html', {'path': path})
    else:
        # If no path is selected, raise an error or redirect
        messages.error(request, "Please select a path to proceed.")
        return redirect('home')

# Progress Page
def progress_view(request):
    return render(request, 'progress.html')  # Progress page


# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')  # Login page


# Register View
def register_view(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Set username to email for simplicity
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}
    return render(request, 'register.html', context)  # Register page


# Logout View
def logoutUser(request):
    logout(request)
    return redirect('home')


# Dynamic Content View
def dynamic_content_view(request, content_type):
    """Handles loading of dynamic content (videos, resources, or projects)."""
    path_id = request.GET.get('path_id')  # Get the path ID from query parameters

    if not path_id:
        raise Http404("Path ID is missing or invalid.")  # Handle missing path_id gracefully

    path = get_object_or_404(Path, id=path_id)  # Ensure the path exists

    # Determine content type and fetch the relevant data
    if content_type == 'videos':
        content = path.videos.all()  # Fetch all videos for the selected path
    elif content_type == 'resources':
        content = path.resources.all()  # Fetch all resources for the selected path
    elif content_type == 'projects':
        content = path.projects.all()  # Fetch all projects for the selected path
    else:
        raise Http404("Invalid content type selected.")  # Handle invalid content types

    return render(request, 'dynamic_content.html', {
        'path': path,
        'content_type': content_type,
        'content': content,
    })
