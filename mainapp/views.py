from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required
from .forms import AlumniForm
from .models import Alumni
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse


def is_hod(user):
    return user.is_staff
@login_required
def hod_dashboard(request):
    return render(request, 'hod_dashboard.html')
@login_required
def hod_add_alumni(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AlumniForm()

    return render(request, 'hod.html', {'form': form})

from .models import Alumni
def home(request):
    total = Alumni.objects.count()
    return render(request, 'home.html', {'total_alumni': total})


def alumni_list(request):
    query = request.GET.get('q')
    dept = request.GET.get('dept')
    year = request.GET.get('year')

    alumni = Alumni.objects.all()

    if query:
        alumni = alumni.filter(name__icontains=query)

    if dept:
        alumni = alumni.filter(department__icontains=dept)

    if year:
        alumni = alumni.filter(graduation_year=year)

    return render(request, 'alumni_list.html', {'alumni': alumni})

def alumni_detail(request, id):
    alumni = Alumni.objects.get(id=id)
    return render(request, 'alumni_detail.html', {'alumni': alumni})
@login_required
def notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications.html', {
        'notifications': notifications
    })


def logout_view(request):
    logout(request)
    return redirect('/')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
from django.shortcuts import render

def placements(request):
    return render(request, 'placements.html')
def hod_login(request):
    return render(request, 'hod_login.html')
from django.contrib.auth.decorators import login_required
from .forms import AlumniForm



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AlumniForm

@login_required
def add_alumni(request):

    if not request.user.is_staff:   # only HOD
        return HttpResponse("You are not allowed")

    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumni_list')
    else:
        form = AlumniForm()

    return render(request, 'add_alumni.html', {'form': form})

def alumni_detail(request, id):
    alumni = Alumni.objects.get(id=id)
    return render(request, 'alumni_detail.html', {'alumni': alumni})
@login_required
def edit_alumni(request, id):
    alumni = Alumni.objects.get(id=id)
    form = AlumniForm(request.POST or None, request.FILES or None, instance=alumni)
    
    if form.is_valid():
        form.save()
        return redirect('alumni_list')

    return render(request, 'edit_alumni.html', {'form': form})
@login_required
def delete_alumni(request, id):
    alumni = Alumni.objects.get(id=id)
    alumni.delete()
    return redirect('alumni_list')
def alumni_detail(request, id):
    alumni = Alumni.objects.get(id=id)
    return render(request, 'alumni_detail.html', {'alumni': alumni})
