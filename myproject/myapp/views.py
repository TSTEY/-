from django.shortcuts import render,redirect,get_object_or_404
from .import models
from . import forms

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
    footer = models.Footer.objects.all()
    return render(request,'admin/footer.html',{'footer':footer})


# Header
def create_header(request):
    if request.method == 'POST':
        form = forms.HeaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('header')
    else:
        form = forms.HeaderForm()
    return render(request, 'admin/form.html',{'form':form})

def update_header(request,user_id):
    user = get_object_or_404(models.Header,id=user_id)
    if request.method == 'POST':
        form = forms.HeaderForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('header')
    else:
        form = forms.HeaderForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_header(request,user_id):
    user = get_object_or_404(models.Header,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('header')
    return render(request,'admin/delete.html',{'user':user})


# Block
# One
def create_block_one(request):
    if request.method == 'POST':
        form = forms.BlockOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_one')
    else:
        form = forms.BlockOneForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_one(request,user_id):
    user = get_object_or_404(models.BlockOne,id=user_id)
    if request.method == 'POST':
        form = forms.BlockOneForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_one')
    else:
        form = forms.BlockOneForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_one(request,user_id):
    user = get_object_or_404(models.BlockOne,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_one')
    return render(request,'admin/delete.html',{'user':user})

# Two
def create_block_two(request):
    if request.method == 'POST':
        form = forms.BlockTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_two')
    else:
        form = forms.BlockTwoForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_two(request,user_id):
    user = get_object_or_404(models.BlockTwo,id=user_id)
    if request.method == 'POST':
        form = forms.BlockTwoForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_two')
    else:
        form = forms.BlockTwoForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_two(request,user_id):
    user = get_object_or_404(models.BlockTwo,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_two')
    return render(request,'admin/delete.html',{'user':user})

# Three
def create_block_three(request):
    if request.method == 'POST':
        form = forms.BlockThreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_three')
    else:
        form = forms.BlockThreeForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_three(request,user_id):
    user = get_object_or_404(models.BlockThree,id=user_id)
    if request.method == 'POST':
        form = forms.BlockThreeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_three')
    else:
        form = forms.BlockThreeForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_three(request,user_id):
    user = get_object_or_404(models.BlockThree,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_three')
    return render(request,'admin/delete.html',{'user':user})

# Four
def create_block_four(request):
    if request.method == 'POST':
        form = forms.BlockFourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_four')
    else:
        form = forms.BlockFourForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_four(request,user_id):
    user = get_object_or_404(models.BlockFour,id=user_id)
    if request.method == 'POST':
        form = forms.BlockFourForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_four')
    else:
        form = forms.BlockFourForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_four(request,user_id):
    user = get_object_or_404(models.BlockFour,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_four')
    return render(request,'admin/delete.html',{'user':user})

# Five
def create_block_five(request):
    if request.method == 'POST':
        form = forms.BlockFiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_five')
    else:
        form = forms.BlockFiveForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_five(request,user_id):
    user = get_object_or_404(models.BlockFive,id=user_id)
    if request.method == 'POST':
        form = forms.BlockFiveForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_five')
    else:
        form = forms.BlockFiveForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_five(request,user_id):
    user = get_object_or_404(models.BlockFive,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_five')
    return render(request,'admin/delete.html',{'user':user})

# Six
def create_block_six(request):
    if request.method == 'POST':
        form = forms.BlockSixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_six')
    else:
        form = forms.BlockSixForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_six(request,user_id):
    user = get_object_or_404(models.BlockSix,id=user_id)
    if request.method == 'POST':
        form = forms.BlockSixForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_six')
    else:
        form = forms.BlockSixForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_six(request,user_id):
    user = get_object_or_404(models.BlockSix,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_six')
    return render(request,'admin/delete.html',{'user':user})

# Seven
def create_block_seven(request):
    if request.method == 'POST':
        form = forms.BlockSevenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_seven')
    else:
        form = forms.BlockSevenForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_seven(request,user_id):
    user = get_object_or_404(models.BlockSeven,id=user_id)
    if request.method == 'POST':
        form = forms.BlockSevenForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_seven')
    else:
        form = forms.BlockSevenForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_seven(request,user_id):
    user = get_object_or_404(models.BlockSeven,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_seven')
    return render(request,'admin/delete.html',{'user':user})

# Eight
def create_block_eight(request):
    if request.method == 'POST':
        form = forms.BlockEightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_eight')
    else:
        form = forms.BlockEightForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_eight(request,user_id):
    user = get_object_or_404(models.BlockEight,id=user_id)
    if request.method == 'POST':
        form = forms.BlockEightForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_eight')
    else:
        form = forms.BlockEightForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_eight(request,user_id):
    user = get_object_or_404(models.BlockEight,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_eight')
    return render(request,'admin/delete.html',{'user':user})

# Nine
def create_block_nine(request):
    if request.method == 'POST':
        form = forms.BlockNineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_nine')
    else:
        form = forms.BlockNineForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_nine(request,user_id):
    user = get_object_or_404(models.BlockNine,id=user_id)
    if request.method == 'POST':
        form = forms.BlockNineForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_nine')
    else:
        form = forms.BlockNineForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_nine(request,user_id):
    user = get_object_or_404(models.BlockNine,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_nine')
    return render(request,'admin/delete.html',{'user':user})

# Ten 
def create_block_ten(request):
    if request.method == 'POST':
        form = forms.BlockTenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_ten')
    else:
        form = forms.BlockTenForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_ten(request,user_id):
    user = get_object_or_404(models.BlockTen,id=user_id)
    if request.method == 'POST':
        form = forms.BlockTenForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_ten')
    else:
        form = forms.BlockTenForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_ten(request,user_id):
    user = get_object_or_404(models.BlockTen,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_ten')
    return render(request,'admin/delete.html',{'user':user})

# Footer
def create_footer(request):
    if request.method == 'POST':
        form = forms.FooterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('footer')
    else:
        form = forms.FooterForm()
    return render(request, 'admin/form.html',{'form':form})

def update_footer(request,user_id):
    user = get_object_or_404(models.Footer,id=user_id)
    if request.method == 'POST':
        form = forms.FooterForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('footer')
    else:
        form = forms.FooterForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_footer(request,user_id):
    user = get_object_or_404(models.Footer,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('footer')
    return render(request,'admin/delete.html',{'user':user})




















