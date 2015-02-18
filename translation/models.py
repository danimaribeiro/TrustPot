from django.utils.translation import ugettext as _
from django.db import models


class Language(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Project(models.Model):

    STATUS = (
        ('new', 'Not cloned'),
        ('cloned', 'To Inspect PO files'),
        ('inspected', 'Inspected'),
        ('error', 'Error cloning'),
    )
    name = models.CharField(max_length=200, unique=True)
    languages = models.ManyToManyField(Language)
    remote = models.CharField(_('Url Remote Repository'),
                              max_length=360, blank=True)
    save_path = models.CharField(_('Repository Path'), max_length=300, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='new')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Template(models.Model):

    name = models.CharField(max_length=200)
    path = models.CharField(max_length=300)
    full_path = models.CharField(max_length=400, blank=True)
    project = models.ForeignKey(Project)

    def file_name(self):
        return self.path + self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class TranslationFile(models.Model):

    name = models.CharField(max_length=200)
    path = models.CharField(max_length=300)
    full_path = models.CharField(max_length=400, blank=True)
    project = models.ForeignKey(Project)

    def file_name(self):
        return self.path + self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Translation(models.Model):

    STATUS = (
        ('not_translated', 'Not Translated'),
        ('needs_review', 'Needs Review'),
        ('reviewed', 'Reviewed'),
    )
    original_text = models.CharField(_('Text'), max_length=5000)
    translated_text = models.CharField(_('Translation'), max_length=5000)
    status = models.CharField(_('Status'), max_length=20, choices=STATUS)

    original_file = models.ForeignKey(TranslationFile)


