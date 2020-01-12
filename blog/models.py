from django.db import models
from django.utils import timezone


class NewTestCase(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.CharField(max_length=200)
    goals = models.TextField()
    requirements = models.TextField()
    TEST_CASE_STAGES = [
        ('ds', 'Design'),
        ('rd', 'Ready'),
        ('dt', 'Delete'),
        ('ft', 'FixIt'),
    ]
    stage = models.CharField(
        max_length=2,
        choices=TEST_CASE_STAGES,
        default='ds',
    )
    pre_conditions = models.TextField()
    variants = models.TextField()
    steps = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    