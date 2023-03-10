OpenCAM
=======

OpenCAM is an open source security camera program.
It supports (or will support) the following features:
 - Video capture
 - True local storage
 - Motion detection
 - TODO Web interface
 - TODO Long and short term storage (Full resolution for 30 days, then optionally lower resolution to save disk space)
 - Free and Open Source Software
 - Notification backend using Discord

Hardware requirements:
 - Computer / Raspberry PI / something capable of running Linux
 - Webcam

Software requirements:
 - Linux (any type)
 - OpenCV (reasonable version, probably 4+)
 - Numpy (Probably 1.2+)
 - python3 (3.8+)
 - Python dotenv

It's possible to satisfy the above requirements on any other UNIX-like operating system, (FreeBSD, OpenBSD, etc) but this project was built with Linux, to run on Linux, so Linux is what is supported.

Note: as much as possible, you should use the system package manager to satisfy the software requirements. Pip leaves an unmanageable mess of files everywhere, making it hard to debug versioning errors.

Tested on AlmaLinux and Fedora (latest Fedora, Almalinux Emerald Puma)

Usage:

Clone the repository, install dependencies, then run make init followed by make

