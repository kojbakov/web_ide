from django.db import models
from django.utils import timezone



class TestCaseTag(models.Model):
    tag = models.CharField(max_length=1000)
    #test_case = models.ForeignKey(NewTestCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']


class NewTestCase(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #tags = models.CharField(max_length=200)
    tags = models.ForeignKey(TestCaseTag, on_delete=models.CASCADE)
    goals = models.TextField()
    requirements = models.TextField()
    TEST_CASE_STAGES = [
        ('Design', 'Design'),
        ('Ready', 'Ready'),
        ('Delete', 'Delete'),
        ('FixIt', 'FixIt'),
    ]
    stage = models.CharField(
        max_length=6,
        choices=TEST_CASE_STAGES,
        default='Design',
    )
    pre_conditions = models.TextField()
    variants = models.TextField()
    #steps = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #step_name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
class MyModel(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    extra_fields = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        

class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name


class StepsResults(models.Model):
    # это поле необходимо для связи с таблицей пользователя
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    # текст сообщения пользователя.
    test_case = models.ForeignKey(NewTestCase, on_delete=models.CASCADE)
    step = models.CharField(max_length=1000)
    result = models.CharField(max_length=1000)
    #chain_test_id = models.CharField(max_length=1000)


class Case(models.Model):
    title = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return "%s %s" % (self.title, self.tags)

class Steps(models.Model):

    step = models.CharField(max_length=1000)
    result = models.CharField(max_length=1000)
    test_case = models.ForeignKey(NewTestCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.step

    class Meta:
        ordering = ['step','result']







'''
case1 = Case.objects.create(title="Андрей")  # создали пользователя
st1 = Steps.objects.create(user=case1, step="шаг 1", res="result 1")  # создали пару сообщений
st2 = Steps.objects.create(user=case1, step="шаг 2", res="result 2")  # создали пару сообщений
# таким способом можно находить все сообщения данного пользователя
messages = Message.objects.filter(user=user1)
'''
