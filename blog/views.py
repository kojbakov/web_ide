from django.utils import timezone
from .models import NewTestCase, Steps, Tag
from .forms import TestCaseForm
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
import re


def tests_list(request):
    # if request.method == "POST" :
    #     if len(request.POST['tags'])>0:
    #         req_tags = request.POST['tags'].replace(' ', '')
    #         if req_tags.endswith(','):
    #             req_tags = req_tags[:-1]
    #         req_tags = req_tags.split(',')
    #         test_id_set = set(map(lambda tag: tag.test_case_id, Tag.objects.filter(tag__in = req_tags)))
    #         posts = NewTestCase.objects.filter(id__in=test_id_set)
    #         tags = Tag.objects.filter()
    #     else:
    #         posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('id')
    #         tags = Tag.objects.filter()
    # else:
    #     posts = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('id')
    #     tags = Tag.objects.filter()
    # loging(posts)
    # tags = Tag.objects.all()
    # return render(request, 'blog/test_list.html', {'posts' : posts,
    #                                                 'tags' : tags})
    tests = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('id')
    tags = Tag.objects.all()
    return render(request, 'blog/tests_list.html', {'tests' : tests, 'tags' : tags})




def test_detail(request, pk):
    test = get_object_or_404(NewTestCase, pk=pk)
    tags = Tag.objects.filter(tags__id=pk)
    steps = Steps.objects.filter(test_case_id=pk).order_by()
    #loging(steps)
    return render(request, 'blog/test_detail.html', {
                            'test' : test,
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
        test_case.tag.set(form.cleaned_data['tag'])
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
        return redirect('test_detail', pk=test_case.pk)
    else:
        form = TestCaseForm()
    return render(request, 'blog/test_new.html', {'form' : form})


def test_edit(request, pk):
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
   

def test_delete(request, pk):
    test = get_object_or_404(NewTestCase, pk=pk)  
    test.delete()
    tests = NewTestCase.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return redirect('tests_list')














