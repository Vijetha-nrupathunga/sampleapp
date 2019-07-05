from django.contrib import admin
from home.models import student,college,library,fee,teacher,book,Section

#from .models import students
#from account.models import AcccInfo 
# Register your models here.

#admin.site.register(student)
#admin.site.register(library)
#admin.site.register(college)
#admin.site.register(fee)
#admin.site.register(teacher)
#admin.site.register(book)

@admin.register(book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(student)
class studentadmin(admin.ModelAdmin):
    search_fields=('student_name','id')
    list_filter=('student_name','department','timestamp')
    fields=('student_name','department','photo','student_usn','subject')

@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(library)
class TeacherAdmin(admin.ModelAdmin):
    pass

