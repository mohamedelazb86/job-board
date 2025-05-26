from django.shortcuts import render
from job.models import Job,Category
from django.db.models import Count

def index(request):
    jobs=Job.objects.all()[:10]
    category=Category.objects.annotate(job_count=Count('job_category'))


    context={
        'jobs':jobs,
        'category':category
    }

    return render(request,'home/index.html',context)
