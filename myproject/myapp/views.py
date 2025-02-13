from django.shortcuts import render
from .import models
def index(request):
    return render(request,'index.html')

def service_details(request):
    return render(request,'service_details.html')

def starter_page(request):
    return render(request,'starter_page.html')

def admin(request):
    return render(request,'admin/admin.html')

def header(request):
    header = models.Header.objects.all()
    return render(request,'admin/header.html',{'header':header})

def block_one(request):
    block_one = models.BlockOne.objects.all()
    return render(request,'admin/Block/one.html',{'block_one':block_one})

def block_two(request):
    block_two = models.BlockTwo.objects.all()
    return render(request,'admin/Block/two.html',{'block_two':block_two})

def block_three(request):
    block_three = models.BlockThree.objects.all()
    return render(request,'admin/Block/three.html',{'block_three':block_three})

def block_four(request):
    block_four = models.BlockFour.objects.all()
    return render(request,'admin/Block/four.html',{'block_four':block_four})

def block_five(request):
    block_five = models.BlockFive.objects.all()
    return render(request,'admin/Block/five.html',{'block_five':block_five})

def block_six(request):
    block_six = models.BlockSix.objects.all()
    return render(request,'admin/Block/six.html',{'block_six':block_six})

def block_seven(request):
    block_seven = models.BlockSeven.objects.all()
    return render(request,'admin/Block/seven.html',{'block_seven':block_seven})

def block_eight(request):
    block_eight = models.BlockEight.objects.all()
    return render(request,'admin/Block/eight.html',{'block_eight':block_eight})

def block_nine(request):
    block_nine = models.BlockNine.objects.all()
    return render(request,'admin/Block/nine.html',{'block_nine':block_nine})

def block_ten(request):
    block_ten = models.BlockTen.objects.all()
    return render(request,'admin/Block/ten.html',{'block_ten':block_ten})

def footer(request):
    footer = models.BlockTen.objects.all()
    return render(request,'admin/footer.html',{'footer':footer})





