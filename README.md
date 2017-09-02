# plex-stieve
Plex Plugin to view Medialaan channels (VTM, Q2, Vitaya, VTM Kzoom, Kadet, CAZ) live using Stievie FREE. Now also supporting Stievie Premium.

# Installation Instructions
Before we start, the plugin requires a valid Stieve account (a free accounts is sufficient). If you don't have an account yet, start by [signing up](https://stievie.be/register.html).

The installation does not require additional steps compared with the installation of other plugins.
1. Download a copy of the repository as ZIP file and unzip.
2. Download a copy of [requests](https://github.com/requests/requests) and unzip it under 'Stievie.bundle/Contents/Libraries/requests'.
3. Copy Stievie.bundle to the Plex Plugin folder.
4. To be on the safe side, restart the Plex Server.
5. Click the "Channels" menu item in Plex.
6. Hover the Stievie symbol with your mouse and click the settings icon.
6. Fill your Stievie username and password. Specify whether you have a Stievie Premium subscription and Save.

Optional: The number of concurrent views using one account is limited based upon a Device ID. By default a random Device ID is used by this channel. If you know the Device ID of your browser or other viewer, you can specify it in the preferences panel.

# Known Issues
* People using Windows 8(.1), please have a look at [this issue](https://github.com/wernerkarlheisenberg/plex-stieve/issues/3). It turns out that the included python libraries in Plex Media Server differ between platforms.

# Issues
When have problems, please file an issue. To speed up the troubleshooting process, please add a copy of the plugin (com.plexapp.plugins.stievie.log), system (com.plexapp.system.log) and server log (Plex Media Server.log).
