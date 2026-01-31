from django.db import models
from django.contrib import admin
class customer34DB(models.Model):
	orderNo=models.IntegerField(primary_key=True);
	Name=models.CharField(max_length=10);
	placed_time=models.TimeField();
	Email=models.EmailField();
	address=models.CharField(max_length=100);
	Mobile_no=models.IntegerField();
	date=models.DateField();
class customer34DBAdmin(admin.ModelAdmin):
	list_display=['orderNo','Name','placed_time','Email','address','Mobile_no','date'];