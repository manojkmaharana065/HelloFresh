from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()


author = 'Manoj Kumar Maharana'
author_email = 'manoj.pythondeveloper065@gmail.com.com'
repo_name = 'template'



setup(
    name=repo_name,
    version='1.0.0',
    description='Repo For {repo_name} data',
    author=author,
    author_email=author_email,
    packages=find_packages(),
    install_requires=install_reqs,
    include_package_data=True,
    zip_safe=False
)