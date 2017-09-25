Snips Assistant - Basic Skills
======================================

|MIT License|

snips-assistant-basics combines a snips assistant vocabulary zip and a range of snips skills from pypi together with a Snipsfile

Installation
------------
First ensure snips and snipsskills is installed

https://github.com/snipsco/snips-platform-documentation

https://github.com/snipsco/snipsskills


Clone the repository and from inside the top level folder run snipsskills install and snipsskills run.

cd /home/pi
git clone https://github.com/syntithenai/snips-assistant-basics.git
cd snips-assistant-basics
snipsskills install
snipsskills run



Usage
-----
Four skills are included

Maths
"what is 4 plus 2"

Spelling
"spell kitten"

MonitorControl
"turn the monitor on", "turn the monitor off"
"set the monitor volume to 70"
"set the monitor brightness to 100"

UsbPower
"turn on/off usb port 2" !!! Supported hubs only - https://github.com/mvp/uhubctl. By default a raspberry pi, this will turn off all usb power including the microphone and crash snips :(


Contributing
------------

.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
:target: https://raw.githubusercontent.com/snipsco/snips-skill-hue/master/LICENSE.txt
:alt: MIT License

.. _`pip`: http://www.pip-installer.org
.. _`Snips`: https://www.snips.ai
.. _`LICENSE.txt`: https://github.com/snipsco/snips-skill-hue/blob/master/LICENSE.txt
.. _`Contribution Guidelines`: https://github.com/snipsco/snips-skill-hue/blob/master/CONTRIBUTING.rst
.. _snipsskills: https://github.com/snipsco/snipsskills
