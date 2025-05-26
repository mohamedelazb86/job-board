from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .myfilter import JobFilter
from django.core.paginator import Paginator


from .models import Job,Category,Apply
from .forms import ApplyForm,JobForm


def job_list(request):
    jobs=Job.objects.all()
    
    f = JobFilter(request.GET, queryset=jobs)
    jobs=f.qs


    paginator = Paginator(jobs, 3)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'jobs':page_obj,
        'myfilter':f
    }
    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    
    if request.method=='POST':

        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect(f'/job/{slug}')
    else:
        form=ApplyForm()
    context={
        'job':job,
        'form':form
    }
    return render(request,'job/job_detail.html',context)

def add_job(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method == 'POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.job=job
            myform.save()
            return redirect('/job/add_job')
          
    else:
        form=JobForm()

    context={
        'form':form
    }
    return render(request,'job/add_job.html',context)

def eng(request):
    eng=Apply.objects.all()

    paginator = Paginator(eng, 1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'engineer':page_obj
    }
    return render(request,'job/eng.html',context)