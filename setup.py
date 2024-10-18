from distutils.core import setup

setup(name="pypos",
      version="0.0.0",
      description="module for interacting with POS pole displays",
      author="Robbie Nesmith",
      author_email="bobberto1995@gmail.com",
      packages=["pypos"],
      install_requires=["pyserial"])