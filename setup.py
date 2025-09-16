from setuptools import setup, find_packages

setup(
    name='dict_field_redacter',
    version='0.1.0',
    packages=find_packages(),
    description='dict-field-redacter: A utility to redact sensitive fields in dictionaries. Easily sanitize your data by masking fields like passwords, tokens, secrets and more... Good for Log Sanitization, Data Privacy, and Security.',
    author='LEMBO Ilem Nelson',
    author_email='lemboilem@lembo.com',
    url='https://github.com/ilemlembo/dict-field-redacter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
)
