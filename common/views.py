from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mvr_fines_check(request):
    return render(request, 'mvr/fines-check.html')
