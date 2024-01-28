from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'news/h.html')

def sports(request):
    head_msg='sports news'
    msg1='virat achieved milestone'
    msg2='India lost worldcup final'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2}
    return render(request,'news/content.html', context=my_dict)

def politics(request):
    head_msg='politics news'
    msg1='will modi become PM in 2024'
    msg2='Dr. Mohan yadav has elected as new CM of MP'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2}
    return render(request,'news/content.html', context=my_dict)