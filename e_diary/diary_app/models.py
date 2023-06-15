from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Subject(models.Model):
    subject = models.CharField(_("Subject"), max_length=50)

    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})


class Student(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='students'
        )
    subject = models.ForeignKey(
        Subject, 
        verbose_name=_("subject"), 
        on_delete=models.CASCADE
        )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    grade = models.IntegerField(
            _("grade"),
            validators=[MinValueValidator(0), MaxValueValidator(12)]
        )


    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return self.first_name, self.last_name

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class Teacher(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='teachers'
        )
    subject = models.ForeignKey(
        Subject, 
        verbose_name=_("subject"), 
        on_delete=models.CASCADE
        )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)  #dalykas
    

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"pk": self.pk})


class Parent(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='parents'
        )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    student = models.ForeignKey(
        Student, 
        verbose_name=_("student"), 
        related_name='parents',
        on_delete=models.CASCADE) 
    

    class Meta:
        verbose_name = _("parent")
        verbose_name_plural = _("parents")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("parent_detail", kwargs={"pk": self.pk})


