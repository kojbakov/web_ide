from django.shortcuts import render
from django.utils import timezone
from .models import NewTestCase
from django.shortcuts import render, get_object_or_404, render_to_response
from .forms import TestCaseForm
#from .forms import BookModelFormset as TestCaseForm
from django.shortcuts import redirect
from django.forms import formset_factory
from django.contrib.auth.models import User
from django.forms import modelform_factory
#from .forms import MyForm
#from .models import MyModel
# from .forms import BookFormset
#from .forms import StepFormset

#from .models import NewTestCase
from django.shortcuts import render, redirect
from .forms import StepsForm
#from .forms import StepsResultsFormset
from .models import StepsResults
from .models import Case
from .models import Steps
from .forms import TestCase

def post_list(request):
    posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('id')
    return render(request, 'blog/post_list.html', {'posts' : posts})


def post_detail(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)
    steps = Steps.objects.filter(test_case_id=pk)
    return render(request, 'blog/post_detail.html', {
                            'post' : post,
                            'steps' : steps,
                            })


def loging(log_obj):
    with open('log.txt', 'a+') as fp:
        try:
            fp.write(str(log_obj))
            fp.write('\n')
        except Exception as e:
            fp.write(str(e))


def new_test_case(request):
    if request.method == "POST":
        #loging(request.POST)
        form = TestCaseForm(request.POST)
        test_case = form.save(commit=False)
        test_case.author = request.user
        test_case.published_date = timezone.now()
        test_case.save()
        for i in range(len(request.POST.getlist('step_'))):
            step = request.POST.getlist('step_')[i]
            result = request.POST.getlist('result_')[i]
            step_result = Steps.objects.create(
                                        test_case=test_case,
                                        step=step,
                                        result=result)
        return redirect('post_detail', pk=test_case.pk)
    else:
        form = TestCaseForm()
    return render(request, 'blog/post_new.html', {'form' : form})


def post_edit(request, pk):
    test_case = get_object_or_404(NewTestCase, pk=pk)
    steps = Steps.objects.filter(test_case_id=pk)
    count = str(len(steps))
    if request.method == "POST":
        form = TestCaseForm(request.POST, instance=test_case)
        if form.is_valid():
            test_case = form.save(commit=False)
            test_case.author = request.user
            test_case.published_date = timezone.now()
            test_case.save()
            loging(request.POST)
            return redirect('post_detail', pk=test_case.pk)
    else:
        form = TestCaseForm(instance=test_case)
    return render(request, 'blog/post_edit.html', {'form': form, 'steps' : steps, 'count' : count})  
   

def post_delete(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)  
    post.delete()
    posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return redirect('post_list')


def test(request):
    template_name = 'blog/test_page.html'
    tc_form = TestCase()
    if request.method == 'POST':
        case = Case.objects.create(title=request.POST['title'])
        st1 = Steps.objects.create(test_case=case,
                                    step=request.POST['Step'],
                                    result=request.POST['Result'],
                                    author=request.user) 
    return render(
            request, template_name, {
                'tc_form': tc_form,
                })

def tests_list(request):
    template_name = 'blog/tests_list.html'
    tests = Case.objects.all()
    return render(request, template_name, {'tests': tests})












