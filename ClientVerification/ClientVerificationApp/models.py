# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Clientmaster(models.Model):
	accountid = models.BigIntegerField(db_column='AccountId', primary_key=True) # Field name made lowercase.
	livedate = models.DateField(db_column='LiveDate', blank=True, null=True) # Field name made lowercase.
	accountname = models.CharField(db_column='AccountName', max_length=500, blank=True) # Field name made lowercase.
	domainname = models.CharField(db_column='DomainName', max_length=1000, blank=True) # Field name made lowercase.
	contactname = models.CharField(db_column='ContactName', max_length=500, blank=True) # Field name made lowercase.
	emailid = models.CharField(db_column='EmailId', max_length=500, blank=True) # Field name made lowercase.
	phone = models.CharField(db_column='Phone', max_length=100, blank=True) # Field name made lowercase.
	visacctdr = models.FloatField(db_column='VISACCTDR', blank=True, null=True) # Field name made lowercase.
	mastercardcctdr = models.FloatField(db_column='MasterCardCCTDR', blank=True, null=True) # Field name made lowercase.
	netbankingtdr = models.FloatField(db_column='NetBankingTDR', blank=True, null=True) # Field name made lowercase.
	debitcardtdr = models.FloatField(db_column='DebitCardTDR', blank=True, null=True) # Field name made lowercase.
	cashcardtdr = models.FloatField(db_column='CashCardTDR', blank=True, null=True) # Field name made lowercase.
	createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
	updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'clientmaster'
	def __unicode__(self):
		return self.accountname


class Reasonmaster(models.Model):
	id = models.AutoField(db_column='Id', primary_key=True) # Field name made lowercase.
	reason = models.CharField(db_column='Reason', max_length=1000, blank=True) # Field name made lowercase.
	createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
	updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
	reasonCategory = models.CharField(db_column='ReasonCategory', max_length=5, blank=True)
	class Meta:
		managed = False
		db_table = 'reasonmaster'
	def __unicode__(self):
		return self.reason
		
class Callreminders(models.Model):
	id = models.AutoField(db_column='Id', primary_key=True) # Field name made lowercase.
	clientmaster_accountid = models.ForeignKey('Clientmaster', db_column='ClientMaster_AccountId') # Field name made lowercase.
	date = models.DateField(db_column='Date', blank=True, null=True) # Field name made lowercase.
	issent = models.TextField(db_column='IsSent', blank=True) # Field name made lowercase. This field type is a guess.
	createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'callreminders'

class Callunreachablelog(models.Model):
	id = models.IntegerField(db_column='Id', primary_key=True) # Field name made lowercase.
	clientmaster_accountid = models.ForeignKey('Clientmaster', db_column='ClientMaster_AccountId') # Field name made lowercase.
	time = models.DateTimeField(db_column='Time', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'callunreachablelog'
		
class Clientresponse(models.Model):
	id = models.BigIntegerField(db_column='Id', primary_key=True) # Field name made lowercase.
	clientmaster_accountid = models.ForeignKey(Clientmaster, db_column='ClientMaster_AccountId') # Field name made lowercase.
	iswebsiteworking = models.CharField(db_column='IsWebsiteWorking', blank=True, max_length=1) # Field name made lowercase. This field type is a guess.
	iscallpicked = models.CharField(db_column='IsCallPicked', blank=True, max_length=1) # Field name made lowercase. This field type is a guess.
	isonreminder = models.CharField(db_column='IsOnReminder', blank=True, max_length=1) # Field name made lowercase. This field type is a guess.
	wishtocontinue = models.CharField(db_column='WishToContinue', blank=True, max_length=1) # Field name made lowercase. This field type is a guess.
	appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True) # Field name made lowercase.
	additionalemailid = models.CharField(db_column='AdditionalEmailId', max_length=500, blank=True) # Field name made lowercase.
	additionalphone1 = models.CharField(db_column='AdditionalPhone1', max_length=100, blank=True) # Field name made lowercase.
	additioanlphone2 = models.CharField(db_column='AdditioanlPhone2', max_length=100, blank=True) # Field name made lowercase.
	responsedate = models.DateTimeField(db_column='ResponseDate', blank=True, null=True) # Field name made lowercase.
	createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
	updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'clientresponse'
		
class Clientresponsereasons(models.Model):
	id = models.BigIntegerField(db_column='Id', primary_key=True) # Field name made lowercase.
	clientmaster_accountid = models.ForeignKey(Clientmaster, db_column='ClientMaster_AccountId') # Field name made lowercase.
	reasonmaster = models.ForeignKey('Reasonmaster', db_column='ReasonMaster_Id') # Field name made lowercase.
	createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
	updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'clientresponsereasons'		
		
class Terminationinitiationqueue(models.Model):
	id = models.IntegerField(db_column='Id', primary_key=True) # Field name made lowercase.
	clientmaster_accountid = models.ForeignKey(Clientmaster, db_column='ClientMaster_AccountId') # Field name made lowercase.
	createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True) # Field name made lowercase.
	updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'terminationinitiationqueue'		