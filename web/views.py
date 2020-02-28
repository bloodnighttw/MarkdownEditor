from django.shortcuts import render

# Create your views here.
from martor.templatetags import martortags
from .models import Post


def test(request):
    if request.method == 'POST':
        print(request.POST['Content'])
    return render(request,'test.html',{'martortags':martortags,'post':Post})