from distutils.core import setup

setup(
    name="modsync",
    description="Files & directories watcher & synchronizer",
    version="0.1.0",
    url="https://walterdolce@bitbucket.org/walterdolce/modsync",
    author="Walter Dolce",
    author_email="walterdolce@gmail.com",
    packages=["modsync"],
    classifiers=[
        "Programming Language :: Python",
        # TODO License classifier
        # TODO Python versions compatibility classifier
        # TODO OSes compatibility classifier
    ],
    install_requires = ['watchdog']
)
