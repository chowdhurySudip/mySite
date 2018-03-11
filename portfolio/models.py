# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class QA(models.Model): 
	req_date = models.DateTimeField('Request Date')
	question = models.CharField(max_length=50)
	answere = models.CharField(max_length=100)

	def __str__(self):
		return self.question+"/"+self.answere