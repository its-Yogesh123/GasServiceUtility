from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from service.models import ServiceRequest
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def is_support_agent(user):
    return user.groups.filter(name='Support Agents').exists()

@user_passes_test(is_support_agent)
def manage_requests(req):
    all_service_requests=ServiceRequest.objects.all()
    return render(req,'support/all_request.html',{"all_service_requests":all_service_requests})
@user_passes_test(is_support_agent)
def update_request(req,reference_id):
    request = get_object_or_404(ServiceRequest, reference_id=reference_id)
    if(req.method =='POST'):
        new_status=req.POST.get('status')
        request.status=new_status
        request.save()
        return redirect("/support/manage_all")

    else :
        return render(req, 'support/manage_request.html', {'request': request})
