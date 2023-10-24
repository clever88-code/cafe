
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, UpdateView
import asyncio
from core.models import Status
from django.views import View
# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import Application_forms,ApplicationFormEdit  
from core.models import Application, office  
from django.views import View
from django.contrib.auth.decorators import login_required





class RecordView(FormView):
    template_name = 'record.html'
    form_class = Application_forms
    success_url = '/record'
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user_applications = Application.objects.filter(auth_user_id=user_id).exclude(status_application__id=3) #Добовляем исключение для объекта что бы пользователь не видел
        all_offices = office.objects.all()
        form = Application_forms
        context = {
            'all_offices': all_offices,
            'user_applications': user_applications,
            'form': form,
        }
        return render(request, self.template_name, context)
    


def add_orders(request):
    if request.POST:
        form = Application_forms(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()

    return redirect('/record/')


class DeleteApplicationView(View):
    def post(self, request, application_id):
        try:
            application = Application.objects.get(id=application_id)
            if application.auth_user_id == request.user.id:
                #получаем 3 объект из таблици Status
                deleted_status = Status.objects.get(id=3)
                application.status_application = deleted_status
                application.save()
                #application.delete()
                print(f"Заявка {application_id} удалена успешно.") 
        except Application.DoesNotExist:
            pass
        return redirect('/record#record')
    




def Edit_application(request, app_id):

    print(app_id)
    
    try:
        application = Application.objects.get(id=app_id)
    except Application.DoesNotExist:
        application = None  

    if request.method == 'POST':
        form = ApplicationFormEdit(request.POST, instance=application, initial={'number_cab': application.number_cab, 'description': application.description})
        if form.is_valid():
            form.save()
            return redirect('request:record')
    else:
        form = ApplicationFormEdit(instance=application, initial={'number_cab': application.number_cab, 'description': application.description})
        print(form)

    context = {
        'form': form,
        'app': application,
    }
    return render(request, 'record.html', context)







