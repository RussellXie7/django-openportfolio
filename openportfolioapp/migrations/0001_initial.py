# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Price'
        db.create_table('financemanager_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
        ))
        db.send_create_signal('financemanager', ['Price'])

        # Adding model 'Investment'
        db.create_table('financemanager_investment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Company'])),
            ('asset_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.AssetClass'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Currency'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
        ))
        db.send_create_signal('financemanager', ['Investment'])

        # Adding model 'Trade'
        db.create_table('financemanager_trade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('volume', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=6)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('trade_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('memo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('payee', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('portfolio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Portfolio'])),
            ('investment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Investment'])),
            ('transid', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('financemanager', ['Trade'])

        # Adding model 'Portfolio'
        db.create_table('financemanager_portfolio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['financemanager.Portfolio'])),
            ('bm', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='benchmark', null=True, to=orm['financemanager.Portfolio'])),
        ))
        db.send_create_signal('financemanager', ['Portfolio'])

        # Adding model 'AssetClass'
        db.create_table('financemanager_assetclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['financemanager.AssetClass'])),
            ('benchmark', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Portfolio'])),
        ))
        db.send_create_signal('financemanager', ['AssetClass'])

        # Adding model 'GICSSector'
        db.create_table('financemanager_gicssector', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['financemanager.GICSSector'])),
        ))
        db.send_create_signal('financemanager', ['GICSSector'])

        # Adding model 'Company'
        db.create_table('financemanager_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gics_sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.GICSSector'])),
        ))
        db.send_create_signal('financemanager', ['Company'])

        # Adding model 'ListedEquityPrice'
        db.create_table('financemanager_listedequityprice', (
            ('price_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['financemanager.Price'], unique=True, primary_key=True)),
            ('investment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Investment'])),
            ('close', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('adj_close', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('dividend', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('high', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('low', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('open', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=4)),
            ('volume', self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=20, decimal_places=0)),
        ))
        db.send_create_signal('financemanager', ['ListedEquityPrice'])

        # Adding model 'CurrencyPrice'
        db.create_table('financemanager_currencyprice', (
            ('price_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['financemanager.Price'], unique=True, primary_key=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Currency'])),
        ))
        db.send_create_signal('financemanager', ['CurrencyPrice'])

        # Adding model 'Currency'
        db.create_table('financemanager_currency', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True)),
            ('locale_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('financemanager', ['Currency'])

        # Adding model 'TradeAllocation'
        db.create_table('financemanager_tradeallocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('buy_trade', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['financemanager.Trade'])),
            ('sell_trade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Trade'])),
            ('volume', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal('financemanager', ['TradeAllocation'])

        # Adding model 'ListedEquity'
        db.create_table('financemanager_listedequity', (
            ('investment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['financemanager.Investment'], unique=True, primary_key=True)),
            ('ticker', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('exchange_code', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('financemanager', ['ListedEquity'])

        # Adding model 'SavingsAccount'
        db.create_table('financemanager_savingsaccount', (
            ('investment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['financemanager.Investment'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('financemanager', ['SavingsAccount'])

        # Adding model 'DataDefinition'
        db.create_table('financemanager_datadefinition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('investment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Investment'])),
            ('headers', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('skip_rows', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_col', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('memo_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('payee_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('debit_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('credit_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('balance_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('price_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('cost_col', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('date_format', self.gf('django.db.models.fields.CharField')(default='%d/%m/%Y', max_length=10)),
        ))
        db.send_create_signal('financemanager', ['DataDefinition'])

        # Adding model 'TradeDataFile'
        db.create_table('financemanager_tradedatafile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('file_name', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('investment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Investment'])),
            ('portfolio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financemanager.Portfolio'])),
        ))
        db.send_create_signal('financemanager', ['TradeDataFile'])

        # Adding M2M table for field transactions on 'TradeDataFile'
        db.create_table('financemanager_tradedatafile_transactions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tradedatafile', models.ForeignKey(orm['financemanager.tradedatafile'], null=False)),
            ('trade', models.ForeignKey(orm['financemanager.trade'], null=False))
        ))
        db.create_unique('financemanager_tradedatafile_transactions', ['tradedatafile_id', 'trade_id'])


    def backwards(self, orm):
        
        # Deleting model 'Price'
        db.delete_table('financemanager_price')

        # Deleting model 'Investment'
        db.delete_table('financemanager_investment')

        # Deleting model 'Trade'
        db.delete_table('financemanager_trade')

        # Deleting model 'Portfolio'
        db.delete_table('financemanager_portfolio')

        # Deleting model 'AssetClass'
        db.delete_table('financemanager_assetclass')

        # Deleting model 'GICSSector'
        db.delete_table('financemanager_gicssector')

        # Deleting model 'Company'
        db.delete_table('financemanager_company')

        # Deleting model 'ListedEquityPrice'
        db.delete_table('financemanager_listedequityprice')

        # Deleting model 'CurrencyPrice'
        db.delete_table('financemanager_currencyprice')

        # Deleting model 'Currency'
        db.delete_table('financemanager_currency')

        # Deleting model 'TradeAllocation'
        db.delete_table('financemanager_tradeallocation')

        # Deleting model 'ListedEquity'
        db.delete_table('financemanager_listedequity')

        # Deleting model 'SavingsAccount'
        db.delete_table('financemanager_savingsaccount')

        # Deleting model 'DataDefinition'
        db.delete_table('financemanager_datadefinition')

        # Deleting model 'TradeDataFile'
        db.delete_table('financemanager_tradedatafile')

        # Removing M2M table for field transactions on 'TradeDataFile'
        db.delete_table('financemanager_tradedatafile_transactions')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'financemanager.assetclass': {
            'Meta': {'object_name': 'AssetClass'},
            'benchmark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Portfolio']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['financemanager.AssetClass']"})
        },
        'financemanager.company': {
            'Meta': {'object_name': 'Company'},
            'gics_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.GICSSector']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'financemanager.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'locale_code': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'financemanager.currencyprice': {
            'Meta': {'object_name': 'CurrencyPrice', '_ormbases': ['financemanager.Price']},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Currency']"}),
            'price_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['financemanager.Price']", 'unique': 'True', 'primary_key': 'True'})
        },
        'financemanager.datadefinition': {
            'Meta': {'object_name': 'DataDefinition'},
            'balance_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'cost_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'credit_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'date_col': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_format': ('django.db.models.fields.CharField', [], {'default': "'%d/%m/%Y'", 'max_length': '10'}),
            'debit_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'headers': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Investment']"}),
            'memo_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'payee_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'price_col': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'skip_rows': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'financemanager.gicssector': {
            'Meta': {'object_name': 'GICSSector'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['financemanager.GICSSector']"})
        },
        'financemanager.investment': {
            'Meta': {'object_name': 'Investment'},
            'asset_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.AssetClass']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Company']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'financemanager.listedequity': {
            'Meta': {'object_name': 'ListedEquity', '_ormbases': ['financemanager.Investment']},
            'exchange_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'investment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['financemanager.Investment']", 'unique': 'True', 'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'financemanager.listedequityprice': {
            'Meta': {'object_name': 'ListedEquityPrice', '_ormbases': ['financemanager.Price']},
            'adj_close': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'}),
            'close': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'}),
            'dividend': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'}),
            'high': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'}),
            'investment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Investment']"}),
            'low': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'}),
            'open': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'}),
            'price_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['financemanager.Price']", 'unique': 'True', 'primary_key': 'True'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '0'})
        },
        'financemanager.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'bm': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'benchmark'", 'null': 'True', 'to': "orm['financemanager.Portfolio']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['financemanager.Portfolio']"})
        },
        'financemanager.price': {
            'Meta': {'object_name': 'Price'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '-1', 'max_digits': '20', 'decimal_places': '4'})
        },
        'financemanager.savingsaccount': {
            'Meta': {'object_name': 'SavingsAccount', '_ormbases': ['financemanager.Investment']},
            'investment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['financemanager.Investment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'financemanager.trade': {
            'Meta': {'object_name': 'Trade'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Investment']"}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'payee': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Portfolio']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '6'}),
            'trade_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'transid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        'financemanager.tradeallocation': {
            'Meta': {'object_name': 'TradeAllocation'},
            'buy_trade': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['financemanager.Trade']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sell_trade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Trade']"}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        'financemanager.tradedatafile': {
            'Meta': {'object_name': 'TradeDataFile'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Investment']"}),
            'portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financemanager.Portfolio']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'transactions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['financemanager.Trade']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['financemanager']