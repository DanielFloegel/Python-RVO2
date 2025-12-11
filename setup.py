from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize

class BuildRvo2Ext(_build_ext):
    """Builds RVO2 before our module."""
    def run(self):
        import os
        import subprocess

        build_dir = os.path.abspath('build/RVO2')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
            subprocess.check_call(['cmake', '../..', '-DCMAKE_CXX_FLAGS=-fPIC'], cwd=build_dir)
        subprocess.check_call(['cmake', '--build', '.'], cwd=build_dir)

        _build_ext.run(self)

extensions = [
    Extension(
        "rvo2",
        ["src/*.pyx"],
        include_dirs=["src"],
        libraries=["RVO"],
        library_dirs=["build/RVO2/src"],
        extra_compile_args=["-fPIC"],
    ),
]

setup(
    name="pyrvo2",
    version="1.0.0",
    description="Python bindings for RVO2 library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/yourpackage",
    author="Your Name",
    author_email="your.email@example.com",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    cmdclass={'build_ext': BuildRvo2Ext},
    python_requires=">=3.8",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Cython',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Cython',  # Include other dependencies if necessary
    ],
)
