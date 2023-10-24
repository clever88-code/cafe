from django.shortcuts import render, redirect
from core.models import Application, Labs_cabinets, office, Status
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.



@login_required
def lab_cabinet_applications(request):
    # Получить текущего пользователя (лаборанта)
    current_user = request.user
    
    lab_cabinets = Labs_cabinets.objects.filter(worker=current_user)
    cabinet_numbers = [cabinet.cabinet for cabinet in lab_cabinets]
    applications = Application.objects.filter(number_cab__in=cabinet_numbers)

    return render(request, 'labs_applications.html', {'applications': applications})

@login_required
def take_application(request, application_id):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        application = Application.objects.get(id=application_id)

        try:
            lab_cabinet = Labs_cabinets.objects.get(worker=request.user, cabinet=application.number_cab)
        except Labs_cabinets.DoesNotExist:
            return redirect('labs_applications')

        application.status_application = Status.objects.get(id=4)
        application.worker = request.user
        application.save()

       
       

    return redirect('/labs_applications/')


@login_required
def change_application(request, application_id):
    if request.method == 'POST':
        print('xui')
        application_id = request.POST.get('application_id')
        application = Application.objects.get(id=application_id)

        try:
            lab_cabinet = Labs_cabinets.objects.get(worker=request.user, cabinet=application.number_cab)
        except Labs_cabinets.DoesNotExist:
            return redirect('labs_applications')

        application.status_application = Status.objects.get(id=2)
        application.worker = request.user
        application.save()

      
        

    return redirect('/labs_applications/')