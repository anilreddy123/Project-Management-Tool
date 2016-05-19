from django.db import models
from django.contrib.auth.models import User
'''
class Team(models.Model):
    teamname = models.CharField(max_length=20)
    team_creation_date = models.DateTimeField(auto_now_add=True,null=True)

    def __unicode__(self):
        return self.teamname'''

'''
class Users(models.Model):
    username = models.CharField(max_length=30,null=True)
    email   =     models.EmailField()
    firstname = models.CharField(max_length=20,null=True)
    lastname =  models.CharField(max_length=20,null=True)
    # mobile =    models.CharField(max_length=12)
    team    =   models.ForeignKey(Team, null=True)
    designation = models.CharField(max_length=15,null= True)
    password1 = models.CharField(max_length=20,null=True)
    password2 = models.CharField(max_length=20,null=True)

    def __unicode__(self):
        return self.email'''



class Projects(models.Model):
    user = models.ForeignKey(User,null = True)
    project_title = models.CharField(max_length=200)
    project_description = models.CharField(max_length=3000)
    duration = models.CharField(max_length=100, null=True, blank=True)
    project_creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.project_title


class Task(models.Model):
    user = models.ForeignKey(User,null = True)
    project = models.ForeignKey(Projects, blank=True, null=True)
    taskname = models.CharField(max_length=500)
    task_desc = models.CharField(max_length=3000, null=True, blank=True)
    #completed = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return self.taskname



class TaskComments(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    tcommencts = models.CharField(max_length=400)
    tcommencts_reply = models.CharField(max_length=400, null= True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.tcomments






