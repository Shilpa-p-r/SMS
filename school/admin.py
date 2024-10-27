from django.contrib import admin
from .models import Students,Officestaff,Librarian

class StudentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Students, StudentsAdmin)

class OfficestaffAdmin(admin.ModelAdmin):
    pass
admin.site.register(Officestaff, OfficestaffAdmin)

class LibrarianAdmin(admin.ModelAdmin):
    pass
admin.site.register(Librarian, LibrarianAdmin)





