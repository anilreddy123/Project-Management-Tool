from django.shortcuts import render ,render_to_response, HttpResponseRedirect,HttpResponse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.template.loader import render_to_string
from django.template import RequestContext



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form })
    return render_to_response('registration/register.html',variables )

def register_success(request):
    return render_to_response('registration/success.html')



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    user_list = User.objects.all()
    return render_to_response('home.html',{'user':request.user, 'user_list':user_list})



def addproject(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if True: #form.is_valid():
           #user = register.POST.get('user','')
           project_title  = request.POST['p_title']
           project_description = request.POST['p_desc']
           project_creation_date = datetime.now() #request.POST.get('project_creation_date','')
           #start_date = request.POST.get('start_date','')
           #end_date = request.POST.get('end_date','')
           assignee = request.POST['p_assign']
           get_assignee = User.objects.get(username = str(assignee))
           project_obj = Projects(user = get_assignee, project_title = project_title, project_description = project_description,project_creation_date = project_creation_date)
           project_obj.save()
           html = "Project created"
           return HttpResponse(html)

    else:
        # If the request was not a POST, display the form to enter details.
        form = ProjectsForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'assignproject.html')


@csrf_protect
def addtask(request):
    print "Inside task creation"
    task = request.POST['task']
    task_desc = request.POST['task_desc']
    sdate = request.POST['sdate']
    edate = request.POST['edate']
    assignee = request.POST['assigne']
    if assignee == "me":
        get_assignee = request.user
    else:
        get_assignee = User.objects.get(username=str(assignee))
    user = request.user
    create_task = Task(project=get_project, user=user, task=task, task_desc=task_desc, completed=False, start_date=sdate, end_date=edate, assigned_to=get_assignee, created=datetime.now())
    print "task"
    create_task.save()
    return HttpResponse("Task Created")

@csrf_protect
def get_project(request):
    print "Here getproject"
    projects = Projects.objects.filter(user = request.user)
    #projects = Projects.objects.filter(user)

    return render(request,"getproject.html", {'projects':projects,})


@csrf_protect
def get_task(request, id=None):
    print "Here gettask"
    #get_user = User.objects.get(user=request.user)
    get_projects = Projects.objects.filter(user = request.user)
    if id is not None:
        tasks = Task.objects.filter(project = id)
    else:
        tasks = Task.objects.filter(project = get_projects[0])

    html = render_to_string("gettask.html", {'projects':get_projects, 'tasks':tasks, 'user':request.user    })
    return HttpResponse(html)


def delete_task(request, id=None):
    del_task = Task.objects.get(id = id).delete()
    return HttpResponseRedirect("/getproject")


