from django.contrib import admin
from .models import LeaveMessage
# Register your models here.
#admin.site.register(LeaveMessage)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('email', 'name', 'topic')
admin.site.register(LeaveMessage, MessageAdmin)