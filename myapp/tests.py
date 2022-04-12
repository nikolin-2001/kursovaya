from django.test import TestCase
from .models import Discipline

class DisciplineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Discipline.objects.create(name='SOBD', description=
        'Technologies for developing computer programs'
        'that will be used by people to solve various problems '
        'on a computer')

    def test_first_name_label(self):
        discipline=Discipline.objects.get(id=1)
        field_label = discipline._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название дисциплины')

