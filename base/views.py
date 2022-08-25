from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

# def student_page(request):
#     return render(request,'base/student.html')

# def student_page(request):
#     print(request.POST)
#     print(request.FILES)
#     form = StudentForm()
#     context = {
#         'form':form
#     }
    
#     return render(request, 'base/student.html', context)


#! database'e veri eklemek için
def student_page(request):
    form = StudentForm()
    if request.method == "POST":  #!request tipi sorgulanır
        form = StudentForm(request.POST, request.FILES) #!form validasyonu yapılır. db'ye uygun mu
        if form.is_valid():
            student_data =  {
                "first_name" : form.cleaned_data.get("first_name"),
                "last_name" : form.cleaned_data.get("last_name"),
                "number" : form.cleaned_data.get("number"),
                "profile_pic": form.cleaned_data.get("profile_image")
            } #! student tablosundan bu bilgileri eklemek istiyoruz.
        
        # Student.objects.create(**student_data)
        student = Student(**student_data)  
        student.save()
        return redirect('index')     #!name olarak belirttiğim ismi gireriz.
    context = {
        "form" : form
    }
    
    return render(request, 'base/student.html', context)