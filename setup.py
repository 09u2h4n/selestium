from setuptools import setup, find_packages

# Read the contents of the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='selestium',
    version='0.2.2',
    description='A Python module for web scraping with Selenium and BeautifulSoup',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Oğuzhan Yılmaz',
    url='https://github.com/09u2h4n/selestium',
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium',
        'beautifulsoup4'
    ],
    python_requires='>=3.8',
)
