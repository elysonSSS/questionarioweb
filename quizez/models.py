from django.db import models
import random

# Create your models here.

DIFF_CHOICES = (

    ('Facil', 'Facil'),
    ('Intermediario', 'Intermediario'),
    ('Dificil', 'Dificil')

)


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duração em minutos")
    required_score_to_pass = models.IntegerField(
        help_text="Pontuacao necessaria para passar")
    difficulty = models.CharField(
        max_length=60, choices=DIFF_CHOICES, default="Select")

    def __str__(self):
        return f"{self.name} - {self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Questionarios'
