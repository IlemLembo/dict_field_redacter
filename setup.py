from setuptools import setup, find_packages
import os

# Read the README.md for the long description
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='dict_field_redacter',
    version='0.1.3',
    packages=find_packages(),
    description='dict-field-redacter: A utility to redact sensitive fields in dictionaries. Easily sanitize your data by masking fields like passwords, tokens, secrets and more... Good for Log Sanitization, Data Privacy, and Security.',
    long_description=long_description, 
    long_description_content_type="text/markdown",  
    author='LEMBO Ilem Nelson',
    author_email='lemboilem@lembo.com',
    url='https://github.com/ilemlembo/dict-field-redacter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
)
