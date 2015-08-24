from setuptools import setup, find_packages

DIRS_EXCLUDED = ['dist', 'build', 'docs', 'tests']

setup(
  name = 'django-redongo',
  packages = find_packages(exclude=DIRS_EXCLUDED),
  version = '0.1',
  description = 'Django command to run redongo server using settings CONFIG',
  author = 'StoneWork Solutions',
  author_email = 'dev@stoneworksolutions.net',
  url = 'https://github.com/stoneworksolutions/django-redongo',
  download_url = 'https://github.com/stoneworksolutions/django-redongo/tarball/0.1',
  keywords = ['redis', 'mongo', 'django', 'bulks'], # arbitrary keywords
  classifiers = [],
  install_requires = [
	'redongo',
  ]
)
