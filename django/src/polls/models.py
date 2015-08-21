from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    '''
        Class which represents a question which has a series of choices associated with it.
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        '''
        Was this question added within the last day
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    def __str__(self):
        return "%s (%d)" % (self.question_text, self.id)

class Choice(models.Model):
    '''
        Class which represents a chosen answer to the question,
    '''
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text