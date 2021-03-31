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
    name = "wifijammer",
    version = "0.1",
    author = "Mark Jeferson Tumolva",
    description = "Continuously jam all wifi clients and access points within range.",
    keywords = "WiFi 802.11 jammer deauth",
    scripts=['wifijammer'],
    # py_modules=['wifijammer'],
    install_requires=['scapy'],
    long_description="Continuously jam all wifi clients and access points within range.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
