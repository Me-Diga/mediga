import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-mediga",
    version = "1.0.0",
    author = "Mateus de Morais, Breno Mariz",
    author_email = "mateusmorais@hotmail.com.br, breno-mariz@outlook.com",
    description = ("Django project used in GCS class."),
    license = "BSD",
    keywords = "django project mediga gcs",
    url = "https://github.com/Me-Diga/mediga",
    packages=['core', 'default', 'auth', 'message', 'user'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
