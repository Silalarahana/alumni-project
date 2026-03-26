from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required
from .forms import AlumniForm
from .models import Alumni
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Department
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumni, Department, Programme
from django.db.models import Max
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
from .models import Alumni, Notification

from django.shortcuts import render
from .models import Alumni, Notification

from django.shortcuts import render
from .models import Alumni, Notification
from .models import Alumni, SuccessStory
from django.shortcuts import render
from .models import Alumni, SuccessStory

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Alumni, SuccessStory, Notification


def home(request):
    teacher = getattr(request.user, 'teacher', None)
    is_hod = teacher and teacher.role == "HOD"
    is_teacher = teacher and teacher.role == "TEACHER"

    total_alumni = Alumni.objects.count()

    placed_count = Alumni.objects.exclude(company_name__isnull=True).exclude(company_name__exact="").count()
    placement_rate = round((placed_count / total_alumni) * 100, 1) if total_alumni > 0 else 0

    total_recruiters = Alumni.objects.exclude(company_name__isnull=True).exclude(
        company_name__exact=""
    ).values('company_name').distinct().count()

    recruiter_companies = Alumni.objects.exclude(company_name__isnull=True).exclude(
        company_name__exact=""
    ).values('company_name').distinct()[:10]

    success_stories = SuccessStory.objects.count()
    featured_stories = SuccessStory.objects.select_related('alumni')[:3]
    highest_package = Alumni.objects.aggregate(Max('salary'))['salary__max']
    if highest_package:
        highest_package = round(highest_package / 100000, 1) 
    # latest 5 students for homepage
    recent_alumni = Alumni.objects.select_related('department').order_by('-created_at')[:5]

    recent_notifications = Notification.objects.select_related(
        'department', 'created_by'
    ).order_by('-created_at')[:5]

    context = {
        'teacher': teacher,
        'is_hod': is_hod,
        'is_teacher': is_teacher,
        'total_alumni': total_alumni,
        'placement_rate': placement_rate,
        'total_recruiters': total_recruiters,
        'success_stories': success_stories,
        'recent_alumni': recent_alumni,
        'recent_notifications': recent_notifications,
        'recruiter_companies': recruiter_companies,
        'featured_stories': featured_stories,
    
    }
    return render(request, 'home.html', context)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import Alumni, Department


@login_required
def alumni_list(request):
    teacher = getattr(request.user, 'teacher', None)

    if not teacher or teacher.role != "HOD":
        return HttpResponseForbidden("Only HOD can view the full student list.")

    query = request.GET.get('search')
    dept = request.GET.get('dept')
    year = request.GET.get('graduation_year')

    alumni = Alumni.objects.select_related('department', 'programme').all()
    departments = Department.objects.all()

    if query:
        alumni = alumni.filter(name__icontains=query)

    if dept:
        alumni = alumni.filter(department__name=dept)

    if year:
        alumni = alumni.filter(graduation_year=year)

    filters_applied = bool(query or dept or year)

    return render(request, 'alumni_list.html', {
        'alumni': alumni,
        'departments': departments,
        'filters_applied': filters_applied
    })

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import Alumni


@login_required
def alumni_detail(request, pk):
    teacher = getattr(request.user, 'teacher', None)

    if not teacher or teacher.role != "HOD":
        return HttpResponseForbidden("Only HOD can view student details.")

    alumni = get_object_or_404(Alumni, pk=pk)
    return render(request, 'alumni_detail.html', {'alumni': alumni})

def notifications(request):
    notifications = Notification.objects.select_related(
        'department', 'created_by'
    ).order_by('notification_type', '-created_at')

    return render(request, 'notifications.html', {
        'notifications': notifications
    })


def logout_view(request):
    logout(request)
    return redirect('home')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
from django.shortcuts import render

def placements(request):
    return render(request, 'placements.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔥 Role based redirect
            if hasattr(user, 'teacher'):
                if user.teacher.role == "HOD":
                    return redirect('add_alumni')

                elif user.teacher.role == "TEACHER":
                    return redirect('add_notification')

            return redirect('home')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')
from django.contrib.auth.decorators import login_required
from .forms import AlumniForm


from .forms import AlumniForm

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Alumni  # adjust import if your app name differs


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Alumni, Department
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Alumni, Department, Programme

@login_required
def add_alumni(request):
    teacher = getattr(request.user, "teacher", None)
    if not teacher or teacher.role != "HOD":
        messages.error(request, "Access denied. Only HOD can add alumni.")
        return redirect("home")

    departments = Department.objects.all().order_by("name")
    programmes = Programme.objects.all().order_by("name")  # change "name" if your field differs

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        dob = request.POST.get("dob") or None
        gender = request.POST.get("gender") or None
        email = request.POST.get("email", "").strip() or None
        phone = request.POST.get("phone", "").strip() or None

        department_id = request.POST.get("department")
        programme_id = request.POST.get("programme") or None
        admission_year = request.POST.get("admission_year") or None
        graduation_year = request.POST.get("graduation_year") or None

        job_title = request.POST.get("job_title", "").strip() or None
        company_name = request.POST.get("company_name", "").strip() or None
        placement_year = request.POST.get("placement_year") or None
        salary = request.POST.get("salary") or None
        job_status = request.POST.get("job_status") or None
        location = request.POST.get("location", "").strip() or None

        photo = request.FILES.get("photo")
        id_card = request.FILES.get("id_card")

        # validations
        if not name:
            messages.error(request, "Name is required.")
            return redirect("add_alumni")

        if not department_id:
            messages.error(request, "Please select a department.")
            return redirect("add_alumni")

        if not graduation_year or not str(graduation_year).isdigit():
            messages.error(request, "Graduation year must be a number.")
            return redirect("add_alumni")

        department = get_object_or_404(Department, id=department_id)
        programme = Programme.objects.filter(id=programme_id).first() if programme_id else None

        Alumni.objects.create(
            name=name,
            dob=dob,
            gender=gender,
            email=email,
            phone=phone,

            department=department,
            programme=programme,
            admission_year=int(admission_year) if admission_year and str(admission_year).isdigit() else None,
            graduation_year=int(graduation_year),

            job_title=job_title,
            company_name=company_name,
            placement_year=int(placement_year) if placement_year and str(placement_year).isdigit() else None,
            salary=salary,  # DecimalField accepts string like "6.50"
            job_status=job_status,
            location=location,

            photo=photo,
            id_card=id_card,
        )

        messages.success(request, "Alumni record saved successfully.")
        return redirect("alumni_list")

    return render(request, "add_alumni.html", {
        "departments": departments,
        "programmes": programmes,
    })
def alumni_detail(request, id):
    alumni = Alumni.objects.get(id=id)
    return render(request, 'alumni_detail.html', {'alumni': alumni})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumni, Department, Programme

def edit_alumni(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    departments = Department.objects.all()
    programmes = Programme.objects.all()

    if request.method == "POST":
        alumni.name = request.POST.get("name")
        alumni.email = request.POST.get("email")
        alumni.phone = request.POST.get("phone")
        alumni.graduation_year = request.POST.get("graduation_year")

        department_id = request.POST.get("department")
        programme_id = request.POST.get("programme")

        if department_id:
            alumni.department = Department.objects.get(id=department_id)

        if programme_id:
            alumni.programme = Programme.objects.get(id=programme_id)

        alumni.save()
        return redirect("alumni_detail", pk=alumni.pk)

    return render(request, "edit_alumni.html", {
        "alumni": alumni,
        "departments": departments,
        "programmes": programmes,
    })
@login_required
def delete_alumni(request, id):
    alumni = Alumni.objects.get(id=id)
    alumni.delete()
    return redirect('alumni_list')
def alumni_detail(request, id):
    alumni = Alumni.objects.get(id=id)
    return render(request, 'alumni_detail.html', {'alumni': alumni})
@login_required
def teacher_dashboard(request):
    teacher = request.user.teacher
    notifications = Notification.objects.filter(department=teacher.department)

    return render(request, 'teacher_dashboard.html', {
        'notifications': notifications
    })

from django.shortcuts import render, redirect
from .models import Notification

def add_notification(request):
    if request.method == "POST":
        title = request.POST.get("title")
        message = request.POST.get("message")
        notification_type = request.POST.get("notification_type")

        Notification.objects.create(
            title=title,
            message=message,
            notification_type=notification_type,
            department=request.user.teacher.department,
            created_by=request.user
        )

        return redirect('notifications')

    return render(request, 'add_notification.html')

    # your existing code
    if request.method == "POST":
        title = request.POST['title']
        message = request.POST['message']

        teacher = request.user.teacher

        Notification.objects.create(
            title=title,
            message=message,
            notification_type=notification_type,
            department=teacher.department,
            created_by=request.user
        )

        return redirect('teacher_dashboard')

    return render(request, 'add_notifications.html')




from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumni, Department, Programme, SuccessStory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumni, Department as DepartmentModel, Programme as ProgrammeModel, SuccessStory

def edit_alumni(request, id):
    alumni = get_object_or_404(Alumni, id=id)
    departments = DepartmentModel.objects.all()
    programmes = ProgrammeModel.objects.all()

    if request.method == "POST":
        alumni.name = request.POST.get('name')

        dob = request.POST.get('dob')
        alumni.dob = dob if dob else None

        alumni.gender = request.POST.get('gender')
        alumni.email = request.POST.get('email')
        alumni.phone = request.POST.get('phone')

        alumni.department_id = request.POST.get('department') or None
        alumni.programme_id = request.POST.get('programme') or None
        alumni.admission_year = request.POST.get('admission_year') or None
        alumni.graduation_year = request.POST.get('graduation_year') or None

        alumni.job_title = request.POST.get('job_title')
        alumni.company_name = request.POST.get('company_name')
        alumni.placement_year = request.POST.get('placement_year') or None
        alumni.salary = request.POST.get('salary') or None
        alumni.job_status = request.POST.get('job_status')
        alumni.location = request.POST.get('location')

        if request.FILES.get('photo'):
            alumni.photo = request.FILES.get('photo')

        if request.FILES.get('id_card'):
            alumni.id_card = request.FILES.get('id_card')

        alumni.save()
        return redirect('alumni_detail', id=alumni.id)

    context = {
        'alumni': alumni,
        'departments': departments,
        'programmes': programmes,
    }

    return render(request, 'edit_alumni.html', context)


    from .models import Department
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def add_department(request):

    teacher = getattr(request.user, "teacher", None)

    if not teacher or teacher.role != "HOD":
        return redirect("home")

    if request.method == "POST":
        name = request.POST.get("name")

        Department.objects.create(name=name)

        return redirect("alumni_list")

    return render(request, "add_department.html")





from django.shortcuts import render, get_object_or_404
from .models import Notification

from django.shortcuts import render, get_object_or_404

def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    return render(request, 'notification_detail.html', {'notification': notification})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Notification

@login_required
def edit_notification(request, pk):
    teacher = getattr(request.user, 'teacher', None)

    if not teacher or teacher.role != "TEACHER":
        return HttpResponseForbidden("Only teachers can edit notifications.")

    notification = get_object_or_404(Notification, pk=pk)

    if request.method == "POST":
        notification.title = request.POST.get("title")
        notification.message = request.POST.get("message")
        notification.notification_type = request.POST.get("notification_type")
        notification.save()
        return redirect('notifications')

    return render(request, 'edit_notification.html', {'notification': notification})


@login_required
def delete_notification(request, pk):
    teacher = getattr(request.user, 'teacher', None)

    if not teacher or teacher.role != "TEACHER":
        return HttpResponseForbidden("Only teachers can delete notifications.")

    notification = get_object_or_404(Notification, pk=pk)

    if request.method == "POST":
        notification.delete()
        return redirect('notifications')

    return redirect('notifications')
def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    return render(request, 'notification_detail.html', {'notification': notification})
from django.shortcuts import render

def about_portal(request):
    return render(request, 'about_portal.html')
