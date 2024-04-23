from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from django.http import HttpResponse
from .serializers import fetch
from .models import user_details
from .models import student
from .serializers import student_fetch

@api_view(['POST','GET'])
def index(request,pk):
    if request.method=="GET":
        # Only these fields
        # queryset = user_details.objects.all().values('id', 'username', 'email')  
        # Getting a list of usernames
        # usernames = user_details.objects.all().values_list('username', flat=True)
        # data1 = user_details.objects.get(name=pk) is used to return a single row
        data1 = student.objects.filter(courses=pk)
        return render(request,'index.html',{'data':data1})


@api_view(['POST','GET'])       
def datastore(request):
    if request.method=="POST":
        name=request.data.get('name')
        courses=request.data.get('courses')
        data1={'name':name,'courses':courses}
        serializer=student_fetch(data=data1)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("data added successfully")
    elif request.method=="GET":
        return render(request,"data.html")



@api_view(['POST','GET'])
def hello(request,pk):
    if request.method=="GET":
        data=student.objects.get(pk=pk)
        if data.courses=='fullstack':
            timestamp=[('Monday','9:00 to 12:50','HTML'),('Tuesday','9:00 to 2:30','CSS'),('Wednesday','9:00 to 1:00','Javascript'),('Thursday','9:00 to 5:00','Bootstrap'),('Friday','9:00 to 4:30','PHP')]
            return render(request,'hello.html',{'data':data,'slot':timestamp})
        elif data.courses=='devops':
            timestamp=[('Monday','9:00 to 12:50','Maven'),('Tuesday','9:00 to 2:30','Gradle'),('Wednesday','9:00 to 1:00','Jenkins'),('Thursday','9:00 to 5:00','Ansible'),('Friday','9:00 to 4:30','Testing Tool')]
            return render(request,'hello.html',{'data':data,'slot':timestamp})
