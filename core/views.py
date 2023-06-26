from django.shortcuts import render,redirect
from django.views import View
from .models import Degree,Program,University

# Create your views here.

class DegreeListView(View):
    def get(self,request):
        degrees = Degree.objects.all()
        return render(request,"core/index.html",{'degrees':degrees})

class ProgramsView(View):
    def get(self,request):
        degree = request.GET.get('degree')
        programs = Program.objects.filter(degree=degree)
        context = {"programs":programs}
        return render(request,'core/partials/programs.html',context)
    
class UniversityView(View):
    def get(self,request):
        university = University.objects.all()
        return render(request,'core/university.html',{'university':university})
    
    def post(self,request):
        programs = request.POST.get('programs')
        university = University.objects.filter(programs=programs)
        return render(request,'core/university.html',{'university':university})
