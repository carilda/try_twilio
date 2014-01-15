# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Twilio'
        db.create_table(u'answer_twilio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('sid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'answer', ['Twilio'])


    def backwards(self, orm):
        # Deleting model 'Twilio'
        db.delete_table(u'answer_twilio')


    models = {
        u'answer.twilio': {
            'Meta': {'object_name': 'Twilio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['answer']