from django.contrib import admin
from .models import QueryPost, student

# Register your models here.

class QueryPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time_display')  # Add 'date' and 'time_display' to the list_display

    def time_display(self, obj):
        return obj.date.strftime('%H:%M:%S')  # Format date to include time

    time_display.short_description = 'Time'  # Set a custom column header for 'time_display'

class studentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'Roll_number')


admin.site.register(QueryPost, QueryPostAdmin)
admin.site.register(student,studentAdmin)