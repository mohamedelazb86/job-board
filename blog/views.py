from django.shortcuts import render,redirect
from .models import Post,Category,Review
from .forms import ReviewForm
from django.core.paginator import Paginator



def post_list(request):
    posts=Post.objects.all().order_by('-id')
    categories=Category.objects.all()

    paginator = Paginator(posts, 1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'posts':page_obj,
        'categories':categories,
        
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    reviews=Review.objects.filter(post=post)

    posts=Post.objects.all().order_by('-id')
    categories=Category.objects.all()

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=post
            myform.save()
            return redirect(f'/blog/{slug}')

    else:
        form=ReviewForm()


    context={
        'post':post,
        'form':form,
        'reviews':reviews,
        'posts':posts,
        'categories':categories
    }
    return render(request,'blog/post_detail.html',context)
