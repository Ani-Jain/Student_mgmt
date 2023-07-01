from datetime import datetime
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import School,Student
from django.db.models import Q 


def home(request):
    return render(request,'home.html');

def all_school(request):
    sch = School.objects.all()
    context = {
        'sch': sch 
    }
    print(context)
    return render(request,'view_all_School.html',context);

def add_School(request):

    if request.method == 'POST':
        name = request.POST['name']
        new_sch = School(name = name, hire_date = datetime.now())
        new_sch.save()

        return HttpResponse('School Added Successfully')

    elif request.method == 'GET':
        return render(request,'add_School.html');

    else:
        return HttpResponse("An Exception Occured!!!")

def remove_School(request, sch_id = 0):
    if sch_id:
        try:
            sch_to_be_deleted = School.objects.get(id = sch_id)
            sch_to_be_deleted.delete()
            return HttpResponse("School Removed Successfully")

        except:
            return HttpResponse("Please Enter A Valid School ID")
    
    sch = School.objects.all()
    context = {
        'sch': sch
    }

    return render(request,'remove_School.html',context);

def filter_school(request):
    if request.method == 'POST':
        name = request.POST['name']
    
        schs = School.objects.all()
        if name:
            schs = schs.filter(name__icontains = name)
        
        context = {
            'sch' : schs 
        }
        return render(request, 'view_all_School.html',context)

    elif request.method == 'GET':
        return render(request,'filter_school.html');

    else:
        return HttpResponse('An Exception Occured')



def update_school(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            schs = School.objects.filter(name__icontains = name)
            schs.name = request.POST['new_name']
            for sc in schs:
                sc.save()
            
        context = {
            'sch' : schs 
        }
        return render(request, 'view_all_School.html',context)

    elif request.method == 'GET':
        return render(request,'update_school.html');

    else:
        return HttpResponse('An Exception Occured')
    

####        CRUD for Students       ####

def all_student(request):
    stu = Student.objects.all()
    context = {
        'stu': stu 
    }
    print(context)
    return render(request,'view_all_Student.html',context);


def add_student(request):

    if request.method == 'POST':
        name = request.POST['name']
        enroll = request.POST['enroll']
        school = request.POST['school']
        new_sch = Student(name = name, enrollment = enroll,school = School.objects.get(name__icontains = school))
        new_sch.save()

        return HttpResponse('Student Added Successfully')

    elif request.method == 'GET':
        sch = School.objects.all()
        context = {
        'sch': sch 
            }
        print(context)

        return render(request,'add_student.html',context);

    else:
        return HttpResponse("An Exception Occured!!!")
    

def remove_student(request, stu_id = 0):
    if stu_id:
        try:
            stu_to_be_deleted = Student.objects.get(id = stu_id)
            stu_to_be_deleted.delete()
            return HttpResponse("Student Removed Successfully")

        except:
            return HttpResponse("Please Enter A Valid Student ID")
    
    stu = Student.objects.all()
    context = {
        'stu': stu
    }

    return render(request,'remove_Student.html',context);



def filter_student(request):
    if request.method == 'POST':
        name = request.POST['name']
    
        stu = Student.objects.all()
        if name:
            stu = stu.filter(name__icontains = name)
        
        context = {
            'stu' : stu 
        }
        return render(request, 'view_all_Student.html',context)

    elif request.method == 'GET':
        return render(request,'filter_student.html');

    else:
        return HttpResponse('An Exception Occured')



def update_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            stu = Student.objects.filter(name__icontains = name)
            stu.name = request.POST['new_name']
            for sc in stu:
                sc.save()
            
        context = {
            'sch' : stu 
        }
        return render(request, 'view_all_Student.html',context)

    elif request.method == 'GET':
        return render(request,'update_student.html');

    else:
        return HttpResponse('An Exception Occured')
    