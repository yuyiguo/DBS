"""
DBS Server default configuration file
"""
import os,logging,sys
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
DBSVERSION = os.getenv('DBS3_VERSION')

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

from DBSSecrets import dbs3_l3_i2
from DBSSecrets import dbs3_p2_i2
from DBSSecrets import dbs3_l1_i2
from DBSSecrets import cms_lum_cmscald

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.dangerously_insecure = True
#config.SecurityModule.key_file = os.path.join(ROOTDIR,'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
#config.Webtools.port = 8250
config.Webtools.port = 8787
config.Webtools.log_screen = True
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbs'
#config.Webtools.environment = 'production'
config.Webtools.environment = 'development'


config.component_('dbs')
config.dbs.templates = os.path.join(ROOTDIR,'apps/dbs/data/templates/WMCore/WebTools')
config.dbs.title = 'DBS Server'
config.dbs.description = 'CMS DBS Service'
config.dbs.section_('views')
config.dbs.admin = 'cmsdbs'
config.dbs.default_expires = 900
config.dbs.instances = ['prod/global','dev/global','int/global']

active = config.dbs.views.section_('active')
active.section_('DBSMigrator')
active.DBSMigrator.object = 'WMCore.WebTools.RESTApi'
active.DBSMigrator.section_('model')
active.DBSMigrator.model.object = 'dbs.web.DBSMigrateModel'
active.DBSMigrator.section_('formatter')
active.DBSMigrator.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSMigrator.section_('database')
instances = active.DBSMigrator.database.section_('instances')

ProductionGlobal = instances.section_('prod/global')
ProductionGlobal.dbowner = cms_lum_cmscald['databaseOwner']
ProductionGlobal.version = DBSVERSION
ProductionGlobal.connectUrl = cms_lum_cmscald['connectUrl']['writer']
ProductionGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

DevelopmentGlobal = instances.section_('dev/global')
DevelopmentGlobal.dbowner = cms_lum_cmscald['databaseOwner']
DevelopmentGlobal.version = DBSVERSION
DevelopmentGlobal.connectUrl = cms_lum_cmscald['connectUrl']['writer']
DevelopmentGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

IntegrationGlobal = instances.section_('int/global')
IntegrationGlobal.dbowner = cms_lum_cmscald['databaseOwner']
IntegrationGlobal.version = DBSVERSION
IntegrationGlobal.connectUrl = cms_lum_cmscald['connectUrl']['writer']
IntegrationGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

active.DBSMigrator.section_('security')
security_instances = active.DBSMigrator.security.section_('instances')
security_production_global = security_instances.section_('prod/global')
security_production_global.params = {'dbs' : 'dbsoperator', 'dataops' : 'production operator'}
security_development_global = security_instances.section_('dev/global')
security_development_global.params = {}
security_integration_global = security_instances.section_('int/global')
security_integration_global.params = {}



active.section_('DBSReader')
active.DBSReader.object = 'WMCore.WebTools.RESTApi'
active.DBSReader.section_('model')
active.DBSReader.model.object = 'dbs.web.DBSReaderModel'
active.DBSReader.section_('formatter')
active.DBSReader.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSReader.section_('database')
instances = active.DBSReader.database.section_('instances')

ProductionGlobal = instances.section_('prod/global')
ProductionGlobal.dbowner = cms_lum_cmscald['databaseOwner']
ProductionGlobal.version = DBSVERSION
ProductionGlobal.connectUrl = cms_lum_cmscald['connectUrl']['reader']
ProductionGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

DevelopmentGlobal = instances.section_('dev/global')
DevelopmentGlobal.dbowner = dbs3_p2_i2['databaseOwner']
DevelopmentGlobal.version = DBSVERSION
DevelopmentGlobal.connectUrl = dbs3_p2_i2['connectUrl']['reader']
DevelopmentGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

IntegrationGlobal = instances.section_('int/global')
IntegrationGlobal.dbowner = dbs3_p2_i2['databaseOwner']
IntegrationGlobal.version = DBSVERSION
IntegrationGlobal.connectUrl = dbs3_p2_i2['connectUrl']['reader']
IntegrationGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

active.section_('DBSWriter')
active.DBSWriter.object = 'WMCore.WebTools.RESTApi'
active.DBSWriter.section_('model')
active.DBSWriter.model.object = 'dbs.web.DBSWriterModel'
active.DBSWriter.section_('formatter')
active.DBSWriter.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSWriter.section_('database')
instances = active.DBSWriter.database.section_('instances')

ProductionGlobal = instances.section_('prod/global')
ProductionGlobal.dbowner = cms_lum_cmscald['databaseOwner']
ProductionGlobal.version = DBSVERSION
ProductionGlobal.connectUrl = cms_lum_cmscald['connectUrl']['writer']
ProductionGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

DevelopmentGlobal = instances.section_('dev/global')
DevelopmentGlobal.dbowner = dbs3_p2_i2['databaseOwner']
DevelopmentGlobal.version = DBSVERSION
DevelopmentGlobal.connectUrl = dbs3_p2_i2['connectUrl']['writer']
DevelopmentGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

IntegrationGlobal = instances.section_('int/global')
IntegrationGlobal.dbowner = dbs3_p2_i2['databaseOwner']
IntegrationGlobal.version = DBSVERSION
IntegrationGlobal.connectUrl = dbs3_p2_i2['connectUrl']['writer']
IntegrationGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

active.DBSWriter.section_('security')
security_instances = active.DBSWriter.security.section_('instances')
security_production_global = security_instances.section_('prod/global')
security_production_global.params = {'dbs' : 'dbsoperator', 'dataops' : 'production operator'}
security_development_global = security_instances.section_('dev/global')
security_development_global.params = {}
security_integration_global = security_instances.section_('int/global')
security_integration_global.params = {}


