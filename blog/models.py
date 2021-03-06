from django.db import models
from django.utils import timezone



class Tag(models.Model):
    tag = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True)

    default = 'btn btn-default'
    dark_blue = 'btn btn-primary'
    green = 'btn btn-success'
    blue = 'btn btn-info'
    orange = 'btn btn-warning'
    red = 'btn btn-danger'
    TAG_STYLES = [
        (default, 'default (gray)'),
        (dark_blue, 'dark blue'),
        (green, 'green'),
        (blue, 'blue'),
        (orange, 'orange'),
        (red, 'red'),
    ]
    tag_style = models.CharField(
        max_length = 20,
        choices=TAG_STYLES,
        default=default,
    )
    #style = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']


class NewTestCase(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag, related_name='tags',
                                 help_text="Select a tags for this test-case",
                                 blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Steps(models.Model):

    step = models.CharField(max_length=1000)
    result = models.CharField(max_length=1000)
    test_case = models.ForeignKey(NewTestCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.step

    class Meta:
        ordering = ['step','result']




