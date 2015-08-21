from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    '''
        Admin view to add the choices of a Question.
    '''
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    '''
        Admin view for the question Model
    '''
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ["question_text"]
    
admin.site.register(Question, QuestionAdmin)