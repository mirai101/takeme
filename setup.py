#!/usr/bin/env python2

#######################################################################
#                                                                     #
#                                                                     #
#          Jam all wifi clients and access points within range        #
#                         version 2 of takeme                         #
#                                                                     #
#######################################################################

from setuptools import setup

setup(
    name = "takeme",
    version = "2",
    author = "Mark Jeferson Tumolva",
    description = "Continuously jam all wifi clients and access points within range.",
    keywords = "WiFi 802.11 jammer deauth",
    scripts=['takeme2'],
    # py_modules=['takeme2'],
    install_requires=['scapy'],
    long_description="Continuously jam all wifi clients and access points within range.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
