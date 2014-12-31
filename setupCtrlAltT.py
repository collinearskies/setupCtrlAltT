#!/usr/bin/python

# This script adds the keyboard shortcut Ctrl-Alt-T to
#   launch the terminal on a Raspberry Pi running Raspbian.
#
# On 24 December, 2014, an OS update moved the config file
#   to a new location in ~/.config/openbox/lxde-pi-rc.xml
#   The old config file was at ~/.config/openbox/lxde-rc.xml
#   The formatting of the file also changed.

import re, os

newStyleText = '\
    </keybind>\n\
    <!-- Launch Terminal with Ctrl+Alt+T -->\n\
    <keybind key="A-C-t">\n\
      <action name="Execute">\n\
        <command>lxterminal</command>\n\
      </action>\n\
    </keybind>\n\n\
  </keyboard>'

oldStyleText = \
'</keybind>\n\n\
  <!-- Launch Terminal with Ctrl+Alt+T -->\n\
  <keybind key="A-C-t">\n\
      <action name="Execute">\n\
          <command>lxterminal</command>\n\
      </action>\n\
  </keybind>\n\n\
</keyboard>'


# If the new config file exists, use it
if os.path.isfile(os.path.abspath('.config/openbox/lxde-pi-rc.xml')):
    with open(os.path.abspath('.config/openbox/lxde-pi-rc.xml'), 'rU') as configFile:
        oldFileContent = configFile.read()

    if newStyleText in oldFileContent:
        print 'The shortcut already exists'
    else:
        print 'Adding shorcut to launch lxterminal'
        newFileContents = re.sub('</keybind>\s+</keyboard>', newStyleText, oldFileContent)

        with open(os.path.abspath('.config/openbox/lxde-rc.xml'), 'w') as configFile:
            configFile.write(newFileContents)

        print 'You will need to reboot before the keyboard shortcut will work.'
else:
    # This is legacy support just in case a Pi hasn't been updated to the new style yet.
    with open(os.path.abspath('.config/openbox/lxde-rc.xml'), 'rU') as configFile:
        oldFileContent = configFile.read()

    if oldStyleText in oldFileContent:
        print 'The shortcut already exists'
    else:
        print 'Adding shorcut to launch lxterminal'
        newFileContents = re.sub('</keybind>\s+</keyboard>', oldStyleText, oldFileContent)

        with open(os.path.abspath('.config/openbox/lxde-rc.xml'), 'w') as configFile:
            configFile.write(newFileContents)

        print 'You will need to reboot before the keyboard shortcut will work.'
