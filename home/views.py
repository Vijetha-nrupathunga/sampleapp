from django.shortcuts import render, redirect
from home.forms import studentsearchform,studentEditModelForm,studentcreateform
from home.models import student
from django.contrib import messages

# Create your views here.
def home_view(request):
    if request.method =='POST':
        search=studentsearchform(request.POST)
        print(search)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=student.objects.filter(student_name__contains=value)
            return render(request,'home.html',{'result':result,'form':studentsearchform()}) 
    else:
        form=studentsearchform()
        result=student.objects.all()
        return render(request,'home.html',{'form':form,'result':result})

   
def contact(request):
    request.session['id']='dell laptop'
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def deletestudent(request,id):
    result=student.objects.get(id=id)
    result.delete()
    messages.success(request,'deleted successfully')
    return redirect('/')

def editstudent(request,id):
    print(request.session['id'])
    stud=student.objects.get(id=id)
    if request.method =='POST':
        modelform=studentEditModelForm(request.POST,instance=stud)
        if modelform.is_valid():
            modelform.save()
            return redirect('/')
    else:
        modelform=studentEditModelForm(instance=stud)			
        return render(request,'edit.html',{'form':modelform,'value':'update'})

def createstudent(request):
    if request.method=="POST":
        form=studentcreateform(request.POST)
        if form.is_valid():
            stud=student.objects.create(student_name=form.cleaned_data.get('student_name'),
            department=form.cleaned_data.get('department'))
            stud.save()
            messages.success(request,"created successfully")
            return redirect('/')
    else:
        form=studentcreateform()
        return render(request,'create.html',{'form':form,'value':'create'})




         # form=studentsearchform()
    # msg="hello from django"
    # context={'form':form,'msg':msg}
    # return render(request,'home.html',context)