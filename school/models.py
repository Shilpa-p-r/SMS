from django.db import models
from django.contrib.auth.models import User



class Librarian(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, null=True)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name


class Officestaff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, null=True)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class Students(models.Model):
    ROLE_CHOICES = (
        ('card', 'CARD'),
        ('cash', 'CASH'),
        ('upi_transfer', 'UPI TRANSFER'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=10,null=True)
    roll_no = models.CharField(max_length=10,null=True)
    mobile = models.CharField(max_length=40,null=True)

    cl= models.CharField(max_length=10,choices=classes,default='one')
    book_title = models.CharField(max_length=255, null=True)
    book_borrow_date = models.DateField(null=True)
    return_date = models.DateField(null=True, blank=True)
    bookdue_date = models.DateField(null=True, blank=True)
    student_fees = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_paid = models.DateField(null=True, blank=True)
    pay_duedate = models.DateField( null=True)
    payment_method = models.CharField(max_length=50, choices=ROLE_CHOICES,default='cash', null=True)  # e.g., Cash, Card, Online Transfer
    remark = models.TextField(null=True, blank=True)
    # blank means it's optional
    due_date = models.DateField(null=True)

    status=models.BooleanField(default=False, null=True)
    @property
    def get_name(self):
        return self.username
    @property
    def get_id(self):
        return self.id
    def __str__(self):
        return self.username


