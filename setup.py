from setuptools import setup, find_packages

setup(
    name='selestium',
    version='0.1.1',
    description='A Python module for web scraping with Selenium and BeautifulSoup',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Oğuzhan Yılmaz',
    url='https://github.com/09u2h4n/selestium',
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium',
        'beautifulsoup4'
    ]
)
