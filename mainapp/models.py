from django.db import models
from django.contrib.auth.models import User


# -----------------------
# Department Model
# -----------------------
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------
# Programme Model
# -----------------------
class Programme(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


from django.db import models


class Alumni(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    JOB_STATUS_CHOICES = (
        ('Placed', 'Placed'),
        ('Promoted', 'Promoted'),
        ('Resigned', 'Resigned'),
        ('Higher Studies', 'Higher Studies'),
    )

    # -----------------------------
    # Personal Info
    # -----------------------------
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    email = models.EmailField(null=True, blank=True)

    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    # -----------------------------
    # Educational Info
    # -----------------------------
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        related_name='alumni'
    )

    programme = models.ForeignKey(
        'Programme',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='alumni'
    )

    admission_year = models.IntegerField(null=True, blank=True)

    graduation_year = models.IntegerField()

    # -----------------------------
    # Placement Info
    # -----------------------------
    job_title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    company_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    placement_year = models.IntegerField(
        null=True,
        blank=True
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    job_status = models.CharField(
        max_length=20,
        choices=JOB_STATUS_CHOICES,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # -----------------------------
    # Documents
    # -----------------------------
    photo = models.ImageField(
        upload_to='photos/',
        null=True,
        blank=True
    )

    id_card = models.FileField(
        upload_to='id_cards/',
        null=True,
        blank=True
    )

    # -----------------------------
    # System Fields
    # -----------------------------
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    # -----------------------------
    # Model Options
    # -----------------------------
    class Meta:
        ordering = ['-graduation_year', 'name']
        verbose_name = "Alumni"
        verbose_name_plural = "Alumni Records"

    def __str__(self):
        return f"{self.name} ({self.graduation_year})"

# -----------------------
# Success Story
# -----------------------
class SuccessStory(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alumni.name


# -----------------------
# Teacher Model
# -----------------------
class Teacher(models.Model):

    ROLE_CHOICES = (
        ('HOD', 'HOD'),
        ('TEACHER', 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username


# -----------------------
# Notification Model
# -----------------------
# -----------------------
# Notification Model
# -----------------------
# -----------------------
# Notification Model
# -----------------------
class Notification(models.Model):

    NOTIFICATION_TYPES = (
        ('career', 'Career Guidance'),
        ('exam', 'Exams'),
        ('job', 'Job Opportunity'),
        ('workshop', 'Workshops'),
    )

    title = models.CharField(max_length=200)
    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default='career'
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models


 