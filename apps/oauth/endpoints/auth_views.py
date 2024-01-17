from django.shortcuts import render


def google_login(request):
    """Auth page with google login
    """
    return render(request, 'oauth/google_login.html')