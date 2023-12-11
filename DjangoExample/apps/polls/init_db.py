import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoExample.settings")
import django
django.setup()

from django.db import transaction
from django.utils import timezone

from DjangoExample.apps.polls.models import Question
from DjangoExample.apps.polls.models import Choice



class InitDb(object):

    @classmethod
    def populate_questions_and_choices(cls):
        with transaction.atomic():
            question = Question.objects.create(question_text="What's up?", pub_date=timezone.now())
            question = Question.objects.get(pk=question.id)
            question.refresh_from_db()
            question.choice_set.create(choice_text="Not Much", votes=0)
            question.choice_set.create(choice_text="The Sky", votes=0)

if __name__ == '__main__':
    app = InitDb()
    app.populate_questions_and_choices()
