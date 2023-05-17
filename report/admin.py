from django.contrib import admin
from report.models import Question

from report.models import Question, CommonReport

admin.site.register(Question)
admin.site.register(CommonReport)
