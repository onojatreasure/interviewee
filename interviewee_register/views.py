from django.shortcuts import render, redirect

from .forms import IntervieweeForm
from .models import Interviewee

# Create your views here.


def interviewee_list(request):
    context = {'interviewee_list': Interviewee.objects.all()}
    return render(request, "interviewee_register/interviewee_list.html", context)


def interviewee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = IntervieweeForm()
        else:
            interviewee = Interviewee.objects.get(pk=id)
            form = IntervieweeForm(instance=interviewee)
        return render(request, "interviewee_register/interviewee_form.html", {'form': form})
    else:
        if id == 0:
            form = IntervieweeForm(request.POST)
        else:
            interviewee = Interviewee.objects.get(pk=id)
            form = IntervieweeForm(request.POST,instance= interviewee)
        if form.is_valid():
            form.save()
        return redirect('/interviewee/list')


def interviewee_delete(request,id):
    interviewee = Interviewee.objects.get(pk=id)
    interviewee.delete()
    return redirect('/interviewee/list')