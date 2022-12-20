from setuptools import setup


setup(
    name='finsh',
    version='0.1.4',    
    description='Share files using django',
    url='https://github.com/mohali4/finsh',
    author='mohali hamilton',
    author_email='mahmohamad560@gmail.com',
    license='MIT',
    packages=['finsh','finsh.sad','finsh.shareing'],
    install_requires=['django','requests','termcolor'],
                    

    #classifiers=[
    #    'Development Status :: 1 - Planning',
    #    'Intended Audience :: Science/Research',
    #    'License :: OSI Approved :: BSD License',  
    #    'Operating System :: POSIX :: Linux',        
    #    'Programming Language :: Python :: 2',
    #    'Programming Language :: Python :: 2.7',
    #    'Programming Language :: Python :: 3',
    #    'Programming Language :: Python :: 3.4',
    #    'Programming Language :: Python :: 3.5',
    #],
)
