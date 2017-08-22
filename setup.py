from setuptools import setup


setup(
    name='Flask-Norm',
    version='1.0',
    url='http://categulario.github.io/flask_norm',
    license='MIT',
    author='Abraham Toriz Cruz',
    author_email='categulario@gmail.com',
    description='Flask module for the Norm redis ORM',
    long_description=__doc__,
    packages=['flask_norm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'norm',
    ],
    test_suite = 'flask_norm.tests.test_flask_norm',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
