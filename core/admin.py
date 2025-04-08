from django.contrib import admin
from .models import Answer, Question

admin.site.site_header = "Quora Clone Admin"
admin.site.site_title = "Quora Clone Admin Portal"
admin.site.index_title = "Welcome to Quora Clone Admin Portal"
admin.site.empty_value_display = '-empty-'
admin.site.site_url = None
admin.site.enable_nav_sidebar = False

admin.site.register(Question)
admin.site.register(Answer)
