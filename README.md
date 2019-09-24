# docker-tegra-qt
Small prototype pyside2/qt application on arm64/tegra

## Goal of the project

This is a small qt application to test qt functionality and link
other tests from other services.

Ideally this can be used as a starting point for a software and hardware
test suite.


## Getting started

Currently you need to build locally the following services:

- docker-tegra-gst 
- docker-tegra-session-dbus 

Out of the box it is configured to run with eglfs, so before running
you should stop lightdm to avoid DRM issues.

Then just run `docker-compose up`.


## Known issues
 

