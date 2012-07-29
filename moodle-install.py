#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import argparse
import re

from lib import config, db, moodle, workplace
from lib.tools import debug, process

DB = db.DB
C = config.Conf().get
Wp = workplace.Workplace()

# Arguments
parser = argparse.ArgumentParser(description='Install a Moodle instance')
parser.add_argument('-i', '--integration', action='store_true', help='create an instance from integration')
parser.add_argument('-e', '--engine', action='store', choices=['mysqli', 'pgsql'], default=C('defaultEngine'), help='database engine to use', metavar='engine')
parser.add_argument('-s', '--suffix', action='store', help='suffix for the instance name', metavar='suffix')
parser.add_argument('-v', '--version', action='store', choices=['19', '20', '21', '22', '23', 'master'], default='master', help='version of Moodle', metavar='version')
parser.add_argument('--interactive', action='store_true', help='interactive mode')
parser.add_argument('--no-install', action='store_true', help='disable the installation', dest='noinstall')
args = parser.parse_args()

engine = args.engine
version = args.version

cacheStable = os.path.join(C('dirs.cache'), 'moodle.git')
cacheIntegration = os.path.join(C('dirs.cache'), 'integration.git')

# Cloning/caching repositories if necessary
if not os.path.isdir(cacheStable):
	result = process('%s clone %s %s' % (C('git'), C('remotes.stable'), cacheStable))
if not os.path.isdir(cacheIntegration):
	result = process('%s clone %s %s' % (C('git'), C('remotes.integration'), cacheIntegration))

# Wording version
prefixVersion = version
versionNice = version
if version == 'master':
	prefixVersion = C('wording.prefixMaster')
	versionNice = C('wording.master')

# Generating parameters
if args.integration:
	name = C('wording.prefixIntegration') + prefixVersion
	fullname = C('wording.integration') + ' ' + versionNice + ' ' + C('wording.%s' % engine)
	repository = cacheIntegration
else:
	name = C('wording.prefixStable') + prefixVersion
	fullname = C('wording.stable') + ' ' + versionNice + ' ' + C('wording.%s' % engine)
	repository = cacheStable

# Append the suffix
if args.suffix:
	name += C('wording.suffixSeparator') + args.suffix
	fullname += ' ' + args.suffix.replace('-', ' ').replace('_', ' ').title()

installDir = os.path.join(C('dirs.store'), name)
wwwDir = os.path.join(installDir, C('wwwDir'))
dataDir = os.path.join(installDir, C('dataDir'))
linkDir = os.path.join(C('dirs.www'), name)

# Cloning the repository
debug('Preparing instance directories...')
if os.path.isdir(installDir):
	debug('Installation directory exists (%s)' % installDir)
	# sys.exit()

	# if args.interactive:
	# 	pass
	# else:
	# 	if args.force:
	# 		pass
	# 	else:
	# 		pass
else:
	os.mkdir(installDir, 0755)
	os.mkdir(dataDir, 0777)
	if C('useCacheAsRemote'):
		result = process('%s clone %s %s' % (C('git'), repository, wwwDir))
	else:
		shutil.copytree(repository, wwwDir)

# Checking database
debug('Preparing database...')
dbname = re.sub(r'[^a-zA-Z0-9]', '', name).lower()[:28]
db = DB(engine, C('db.%s' % engine))
if db.dbexists(dbname):
	db.dropdb(dbname)
	db.createdb(dbname)
else:
	db.createdb(dbname)
db.selectdb(dbname)

# Installing
if os.path.islink(linkDir):
	os.remove(linkDir)
if os.path.isfile(linkDir) or os.path.isdir(linkDir):	# No elif!
	debug('Could not create symbolic link')
else:
	os.symlink(wwwDir, linkDir)

# Creating, fetch, pulling branches
debug('Setting up repository...')
M = Wp.get(name)
git = M.git()
result = git.fetch('origin')
if version == 'master':
	git.checkout('master')
else:
	track = 'origin/MOODLE_%s_STABLE' % version
	branch = 'MOODLE_%s_STABLE' % version
	git.createBranch(branch, track)
	git.checkout(branch)
git.pull()
git.addRemote('mine', C('remotes.mine'))

# Launching installation process
if not args.noinstall:

	debug('Installing %s...' % name)
	cli = 'admin/cli/install.php'
	params = (C('host'), name, dataDir, engine, dbname, C('db.%s.user' % engine), C('db.%s.passwd' % engine), C('db.%s.host' % engine), fullname, name, C('login'), C('passwd'))
	args = '--wwwroot="http://%s/%s/" --dataroot="%s" --dbtype="%s" --dbname="%s" --dbuser="%s" --dbpass="%s" --dbhost="%s" --fullname="%s" --shortname="%s" --adminuser="%s" --adminpass="%s" --allow-unstable --agree-license --non-interactive' % params
	result = M.cli(cli, args, stdout=None, stderr=None)
	if result[0] != 0:
		raise Exception('Error while running the install, please manually fix the problem.')

	configFile = os.path.join(wwwDir, 'config.php')
	os.chmod(configFile, 0666)
	try:
		M.addConfig('sessioncookiepath', '/%s/' % name)
	except Exception:
		debug('Could not append $CFG->sessioncookiepath to config.php')

debug('Process complete!')
