from django.shortcuts import render
from django.http import JsonResponse
from appointments.models import Appointment
from datetime import datetime

# Create your views here.
def onlypage(request):
    print(request.method)
    if request.method=="GET":
        if request.GET:
            items=Appointment.objects.all()
            search=request.GET.get('search',None)
            if search:
                items=items.filter(description__icontains=search)
            records=[{'date':item.time.date(),'time':item.time.time(), 'description':item.description} for item in items.order_by('time')]
            return JsonResponse({'appointments':records})
        else:
            return render(request,'appointments.html')
    if request.method=="POST":
        datev=request.POST.get('date', None)
        timev=request.POST.get('time',None)
        description=request.POST.get('description',None)
        print('date was: %s, time was: %s, description was %s'%(datev,timev, description))
        if datev and timev and description:
            added=Appointment(time=datetime.strptime(datev+" "+timev, '%Y-%m-%d %H:%M'), description=description)
            added.save()
        return render(request,'appointments.html')
