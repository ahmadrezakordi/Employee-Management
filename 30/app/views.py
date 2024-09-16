from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import *

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class DashboardView(View):
    def get(self, request):
        items = Employee.objects.filter(user=request.user.id).order_by('id')
        context = {'items': items}

        return render(request, 'dashboard.html', context)


def login_redirect(request):
    return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )

            if user is not None:
                login(request, user)
                return redirect('dashboard')
        return render(request, 'register.html', {"form": form})


class AddEmployee(CreateView):
    model = Employee
    form_class = ProfileForm
    template_name = 'employee-form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        self.birth_email()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.all()
        return context

    def birth_email(self):
        today = timezone.now().date()
        employees = Employee.objects.all()

        birthday_today = [employee for employee in employees if employee and employee.birthday.month == today.month and employee.birthday.day == today.day]
        other_employees = [employee for employee in employees if employee not in birthday_today]

        for employee in birthday_today:
            send_mail(
                'Happy Birthday',
                f'Happy Birthday {employee.name}',
                settings.EMAIL_HOST_USER,
                [employee.email],
                fail_silently=False,
                )
        if birthday_today:
            for employee in other_employees:
                for employee2 in birthday_today:
                    send_mail(
                        'Birthday!',
                        f'Hey {employee.name} today is {employee2.name} Birthday',
                        settings.EMAIL_HOST_USER,
                        [employee.email],
                        fail_silently=False,
                        )


class EditEmployee(UpdateView):
    model = Employee
    form_class = ProfileForm
    template_name = 'employee-form.html'
    success_url = reverse_lazy('dashboard')


class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'delete-form.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'