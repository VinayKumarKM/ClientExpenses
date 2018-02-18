from django.db import models

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=250)
	location = models.CharField(max_length=150)

	def __str__(self):
		return self.name


class Expense(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	amount = models.IntegerField()
	currency = models.CharField(max_length=50)
	timestampOfExpense = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.client.name + ' ' + self.title

