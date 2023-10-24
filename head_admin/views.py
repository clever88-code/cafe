from django.shortcuts import render, redirect
from core.models import Application, Status, Labs_cabinets
from django.contrib.auth.decorators import login_required
from django.db.models import Q



@login_required
def applications_by_status(request):
    status1 = Status.objects.get(id=2)
    status2 = Status.objects.get(id=5)
    applications = Application.objects.filter(Q(status_application=status1) | Q(status_application=status2))

    return render(request, 'labs_admin_applications.html', {'applications': applications})


@login_required
def edit_application(request, application_id):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        application = Application.objects.get(id=application_id)
        application.status_application = Status.objects.get(id=5)
        application.worker = request.user
        application.save()

       
    return redirect('/labs_admin_applications/')


@login_required
def archive_application(request, application_id):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        application = Application.objects.get(id=application_id)
        application.status_application = Status.objects.get(id=3)
        application.worker = request.user
        application.save()

       
    return redirect('/labs_admin_applications/')
