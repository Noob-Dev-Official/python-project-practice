# Dancer 2.0

## Minimal-code implementation of Digital Agent Networking for Consumer Energy Reduction

*Copyright S. Dudley, B. Bademci, R. Brown (London South Bank University)*


**Simply run ./config.sh with parameters as root**

* To enable LED software control In BIOS Advanced > Power > Secondary Power Settings set Ring LED to "SW Control"

* If parameter == gateway run

  * `sudo ./config.sh gateway <fixedIPAddress>`

  * e.g. `sudo ./config.sh gateway 10.42.0.1`


* If parameter == sensor run:

`sudo ./config.sh sensor`

*Once it's done reboot for deploying changes.
