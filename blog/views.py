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
from .models import TestCaseTag 
import re
#___
from django.db.models.functions import Lower
from django.http import JsonResponse
from functools import reduce
from django.db.models import Q
import operator


def post_list(request):
    #loging('o')
    #loging(request.POST)
    loging(request)
    if request.method == "POST" :
        #loging(request.POST)
        if len(request.POST['tags'])>0:
            req_tags = request.POST['tags'].replace(' ', '')
            if req_tags.endswith(','):
                req_tags = req_tags[:-1]
            req_tags = req_tags.split(',')
            test_id_set = set(map(lambda tag: tag.test_case_id, TestCaseTag.objects.filter(tag__in = req_tags)))
            posts = NewTestCase.objects.filter(id__in=test_id_set)
            tags = TestCaseTag.objects.filter()
        else:
            posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('id')
            tags = TestCaseTag.objects.filter()
    else:
        posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('id')
        tags = TestCaseTag.objects.filter()

    return render(request, 'blog/post_list.html', {'posts' : posts,
                                                    'tags' : tags})


def post_detail(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)
    tags = TestCaseTag.objects.filter(test_case_id=pk)
    steps = Steps.objects.filter(test_case_id=pk).order_by()
    #loging(steps)
    return render(request, 'blog/post_detail.html', {
                            'post' : post,
                            'tags' : tags,
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
        tags = request.POST.getlist('tags')[0].replace(' ', '')
        tags = tags.split(',')
        #loging(tags)
        for tag in tags:
            TestCaseTag.objects.create(test_case=test_case, tag=tag)
        new_steps_list = request.POST.getlist('step_new')
        new_results_list = request.POST.getlist('result_new')
        # сохранение новых записей о шагах
        for i in range(len(new_steps_list)):
            step = new_steps_list[i]
            result = new_results_list[i]
            Steps.objects.create(
                                test_case=test_case,
                                step=step,
                                result=result)
        return redirect('post_detail', pk=test_case.pk)
    else:
        form = TestCaseForm()
    return render(request, 'blog/post_new.html', {'form' : form})


def post_edit(request, pk):
    test_case = get_object_or_404(NewTestCase, pk=pk)
    tags = TestCaseTag.objects.filter(test_case_id=pk)
    steps = Steps.objects.filter(test_case_id=pk).order_by()
    if request.method == "POST":
        req_tags = request.POST['tags'].replace(' ', '')
        if req_tags.endswith(','):
            req_tags = req_tags[:-1]
        req_tags = req_tags.split(',')
        form = TestCaseForm(request.POST, instance=test_case)
        if form.is_valid():
            test_case = form.save(commit=False)
            test_case.author = request.user
            test_case.published_date = timezone.now()
            test_case.save()
            exist_tags = [str(tag.tag) for tag in tags]
            tags_for_delete = list(set(exist_tags) - set(req_tags))
            new_tags = list(set(req_tags) - set(exist_tags))
            exist_tags_pk = [(tag.tag,tag.pk) for tag in tags]
            new_steps_list = request.POST.getlist('step_new')
            new_results_list = request.POST.getlist('result_new')
            pk_post_list = []
            # удаление старых тегов
            if tags_for_delete:
                for tag_pk in exist_tags_pk:
                    if tag_pk[0] in tags_for_delete:
                        TestCaseTag.objects.filter(pk=tag_pk[1]).delete()
            # добавление новых тегов
            if new_tags:
                for tag in new_tags:
                    TestCaseTag.objects.create(tag=tag,
                                               test_case=test_case)
            for item in request.POST:
                if item not in ['csrfmiddlewaretoken', 'title', 'tags', 'step_new', 'result_new']:
                    if 'result_' not in item:
                        pk_post_list.append(re.findall(r'step_(\d+)', item)[0])
            exist_pk = [str(step.pk) for step in steps]
            pk_for_delete = list(set(exist_pk) - set(pk_post_list))
            pk_for_update = list(set(exist_pk) - set(pk_for_delete))
            # обновление существующих записей о шагах
            for pk_up in pk_for_update:
                step=request.POST.getlist(f'step_{pk_up}')[0]
                result=request.POST.getlist(f'result_{pk_up}')[0]
                Steps.objects.filter(test_case_id=pk,pk=pk_up).update(
                        step=step)
                Steps.objects.filter(test_case_id=pk,pk=pk_up).update(
                    result=result)
            # удаление записей о шагах
            if pk_for_delete:
                for pk_del in pk_for_delete:
                    Steps.objects.filter(test_case_id=pk,pk=pk_del).delete()
            # сохранение новых записей о шагах
            for i in range(len(new_steps_list)):
                step = new_steps_list[i]
                result = new_results_list[i]
                Steps.objects.create(
                                    test_case=test_case,
                                    step=step,
                                    result=result)                
            return redirect('post_detail', pk=test_case.pk)
    else:
        form = TestCaseForm(instance=test_case)
    return render(request, 'blog/post_edit.html', {'form': form, 'tags' : tags, 'steps' : steps})  
   

def post_delete(request, pk):
    post = get_object_or_404(NewTestCase, pk=pk)  
    post.delete()
    posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return redirect('post_list')


def tests_search(request):
    loging(request)
    # loging(request.POST)
    # loging(request.GET)
    # loging('123')
    #return redirect('post_detail')
    #pass
    #return render(request, 'blog/post_list.html', {'posts' : posts})



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












