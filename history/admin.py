from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Publication, Article

admin.site.register(Publication, SimpleHistoryAdmin)
admin.site.register(Article, SimpleHistoryAdmin)