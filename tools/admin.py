from django.contrib import admin

from .models import *

#admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(TaskComments)