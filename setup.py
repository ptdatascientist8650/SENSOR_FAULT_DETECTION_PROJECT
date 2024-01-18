from setuptools import find_packages ,setup


def get_requirements():#to import required libraries for the project 
    pass 

setup(
    name='sensor',
    version='0.0.1',
    author='saurabh_kumar',
    author_email='prajapatisaurabh338@gmail.com',
    packages=find_packages(),#it will identify sensor folder ,we create bcz specific file as  using init file we created .
    #each folder inside init we be consider as a packages 
    install_requires=get_requirements(),
)







