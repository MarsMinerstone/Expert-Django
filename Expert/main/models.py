from django.db import models


class Discipline(models.Model):
	"""docstring for Discipline"""
	d_name = models.CharField(max_length=20, verbose_name='Наименование')
	d_description = models.TextField(verbose_name='Описание', null=True, blank=True)
	d_price = models.IntegerField(verbose_name='Цена обучения', null=True, blank=True)
		
	def __str__(self):
		return self.d_name


class Service(models.Model):
	"""docstring for Service"""
	s_name = models.CharField(max_length=20, verbose_name='Наименование')
	s_description = models.TextField(verbose_name='Описание', null=True, blank=True)
		
	def __str__(self):
		return self.s_name


class Education(models.Model):
	"""docstring for Education"""
	e_name = models.CharField(max_length=20, verbose_name='Наименование')
		
	def __str__(self):
		return self.e_name


class Addition(models.Model):
	"""docstring for Addition"""
	a_name = models.CharField(max_length=20, verbose_name='Наименование')
		
	def __str__(self):
		return self.a_name


class Partner(models.Model):
	"""docstring for Partner"""
	p_name = models.CharField(max_length=20, verbose_name='Наименование')
	p_image = models.ImageField(verbose_name='Лого')
		
	def __str__(self):
		return self.p_name


class Mail(models.Model):
	"""docstring for Mail"""
	e_name = models.CharField(max_length=20, verbose_name='Имя')
	email = models.EmailField(max_length=30)

	def __str__(self):
		return f"{self.e_name} {self.email}"


class Question(models.Model):
	question = models.TextField(verbose_name="Вопрос")
	answer = models.TextField(verbose_name="Ответ")
	is_visible = models.BooleanField(verbose_name="Отображение")

	def __str__(self):
		return self.question
