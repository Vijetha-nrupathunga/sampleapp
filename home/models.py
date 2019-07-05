from django.db import models

# Create your models here.

class student(models.Model):
    #id=models.AutoField()
    student_name=models.CharField('student name', max_length=30,null=True)
    dept=(('ise','information science'),
    ('mh',"mech"),
    ('cv','civil'))
    photo=models.ImageField(upload_to='media/',null=True)
    department=models.CharField('department',choices=dept,blank=True,null=True,max_length=30)
    student_usn=models.CharField('USN',max_length=11,null=True)
    sub=(('fafl','finite automata and formal languages'),('mc','microcontroller'),('ada','analysis and design of algorithm'))
    subject=models.CharField('sub',choices=sub,blank=True,null=True,max_length=40)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name

class teacher(models.Model):
    teacher=models.CharField('teacher name',max_length=100,null=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher

class book(models.Model):
    book=models.CharField('book',max_length=100,null=True)
    def __str__(self):
        return self.book

class Section(models.Model):
    advisor=models.OneToOneField('Teacher',on_delete=models.SET_NULL,null=True)
    students=models.ManyToManyField('Student',null=False)
    section=models.CharField('Section',max_length=30,null=False)
    def __str__(self):
        return self.section


class college(models.Model):
    stu=models.ForeignKey('student',on_delete=models.SET_NULL,null=True)
    clg_name=models.CharField('college',max_length=30,null=True)
    def __str__(self):
        return self.clg_name

class library(models.Model):
    library_name=models.CharField('library',null=True,max_length=100)
    books=models.ManyToManyField('book',null=True)
    def __str__(self):
        return self.library_name




class fee(models.Model):
    fees=models.ForeignKey('student',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.fee

