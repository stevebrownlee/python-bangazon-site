from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')
