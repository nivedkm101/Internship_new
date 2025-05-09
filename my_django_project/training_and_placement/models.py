from django.db import models


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    img = models.CharField(max_length=500, blank=True, null=True)    
    class Meta:
        db_table = 'faculty'
        managed = False
        
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    img = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        db_table = 'staff'
        managed = False  # Tell Django not to manage this table

    def __str__(self):
        return f"{self.name} - {self.designation}"

    @property
    def static_img(self):
        """
        Returns the image path for use with the static template tag.
        Converts 'assets/images/...' to 'images/...'
        Converts 'assets/images/...' to 'static/images/...' if you want to use it directly (not recommended).
        """
        if self.img and self.img.startswith('assets/'):
            # Remove 'assets/' prefix
            return self.img.replace('assets/', '', 1)
        return self.img

    @property
    def email(self):
        # Get email from role if available
        email_role = self.role_set.filter(mail__isnull=False).first()
        return email_role.mail if email_role else None

    @property
    def phone(self):
        # Get phone from role if available
        phone_role = self.role_set.filter(phone__isnull=False).first()
        return phone_role.phone if phone_role else None

class Role(models.Model):
    r_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(Staff, on_delete=models.CASCADE, db_column='id')
    role = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, blank=True, null=True)
    mail = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'role'
        managed = False  # Tell Django not to manage this table

    def __str__(self):
        return f"{self.id.name} - {self.role}"

