from .models import Setting

def get_context_data(request):
    data=Setting.objects.all().last()
    return {'data':data}