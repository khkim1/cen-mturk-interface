from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
import unittest
from project import app, db
import coverage

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
	"""Runs the tests without coverage."""
	tests = unittest.TestLoader().discover('.')
	unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
	"""Runs the tests with coverage."""
	cov = coverage.coverage(branch=True, include='project/*')
	cov.start()
	tests = unittest.TestLoader().discover('.')
	unittest.TextTestRunner(verbosity=2).run(tests)
	cov.stop()
	cov.save()
	print('Coverage Summary')
	cov.report()
	basedir = os.path.abspath(os.path.dirname(__file__))
	covdir = os.path.join(basedir, 'coverage')
	cov.html_report(directory=covdir)
	cov.erase()


if __name__ == '__main__':
	manager.run()
