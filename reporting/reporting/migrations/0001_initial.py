# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mentor'
        db.create_table(u'reporting_mentor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'reporting', ['Mentor'])

        # Adding model 'Enrolling_Party'
        db.create_table(u'reporting_enrolling_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'reporting', ['Enrolling_Party'])

        # Adding model 'Mentee'
        db.create_table(u'reporting_mentee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enrolled_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reporting.Enrolling_Party'])),
            ('enrolled_on', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'reporting', ['Mentee'])

        # Adding model 'Calls'
        db.create_table(u'reporting_calls', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reporting.Mentor'])),
            ('mentee_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reporting.Mentee'])),
            ('call_number', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.TimeField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('num_completed_goals', self.gf('django.db.models.fields.IntegerField')()),
            ('num_active_goals', self.gf('django.db.models.fields.IntegerField')()),
            ('num_completed_action_plans', self.gf('django.db.models.fields.IntegerField')()),
            ('num_active_action_plans', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'reporting', ['Calls'])


    def backwards(self, orm):
        # Deleting model 'Mentor'
        db.delete_table(u'reporting_mentor')

        # Deleting model 'Enrolling_Party'
        db.delete_table(u'reporting_enrolling_party')

        # Deleting model 'Mentee'
        db.delete_table(u'reporting_mentee')

        # Deleting model 'Calls'
        db.delete_table(u'reporting_calls')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'reporting.calls': {
            'Meta': {'object_name': 'Calls'},
            'call_number': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.TimeField', [], {}),
            'mentee_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reporting.Mentee']"}),
            'mentor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reporting.Mentor']"}),
            'num_active_action_plans': ('django.db.models.fields.IntegerField', [], {}),
            'num_active_goals': ('django.db.models.fields.IntegerField', [], {}),
            'num_completed_action_plans': ('django.db.models.fields.IntegerField', [], {}),
            'num_completed_goals': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'reporting.enrolling_party': {
            'Meta': {'object_name': 'Enrolling_Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'reporting.mentee': {
            'Meta': {'object_name': 'Mentee'},
            'enrolled_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reporting.Enrolling_Party']"}),
            'enrolled_on': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'reporting.mentor': {
            'Meta': {'object_name': 'Mentor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['reporting']