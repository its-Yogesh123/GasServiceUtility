from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
@login_required
def new_request(req):
    if req.method == 'POST':
        form = forms.ServiceRequestForm(req.POST, req.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = req.user
            service_request.save()
            return redirect('trace_request', reference_id=service_request.reference_id)
    else:
        form = forms.ServiceRequestForm()
    return render(req, 'service/newService.html', {'form': form})
@login_required
def track_request(req,reference_id=None):
    try:
        service_request = models.ServiceRequest.objects.filter(user=req.user)
    except models.ServiceRequest.DoesNotExist:
        return HttpResponse("Something Went Wrong ..........while traking request")
    if(reference_id):
        try:
            o_req = models.ServiceRequest.objects.get(reference_id=reference_id,user=req.user)
        except models.ServiceRequest.DoesNotExist:
            return HttpResponse("Invaid Refrence ID ")
        return render(req, 'service/traceService.html',{'request':service_request,'user':req.user,'one_request':o_req})
    else:
        return render(req, 'service/traceService.html',{'request':service_request,'user':req.user})
    
