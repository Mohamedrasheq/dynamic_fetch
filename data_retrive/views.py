from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from django.http import HttpResponse
from .serializers import fetch
from .models import user_details
@api_view(['POST','GET'])
def index(request,pk):
    if request.method=="GET":
        # Only these fields
        # queryset = user_details.objects.all().values('id', 'username', 'email')  
        # Getting a list of usernames
        # usernames = user_details.objects.all().values_list('username', flat=True)
        # data1 = user_details.objects.get(name=pk) is used to return a single row
        data1 = user_details.objects.filter(name=pk)
        return render(request,'index.html',{'data':data1})

@api_view(['POST','GET'])       
def datastore(request):
    if request.method=="POST":
        name=request.data.get('name')
        mark=request.data.get('mark')
        college=request.data.get('college')
        data1={'name':name,'mark':mark,'college':college}
        serializer=fetch(data=data1)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("data added successfully")
    elif request.method=="GET":
        return render(request,"data.html")



@api_view(['POST','GET'])
def hello(request):
    if request.method=="GET":
        return render(request,'hello.html')