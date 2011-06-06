#!/bin/sh

# File: uninstall.sh
#
# Version 0.3
# by H Xu
#
# the uninstall script for nautilus-py-vim

INSTALLATION_FOUND=0

for ONE_DIR in\
    '/usr/local/lib64/nautilus/extensions-3.0'\
    '/usr/local/lib64/nautilus/extensions-2.0'\
    '/usr/local/lib/nautilus/extensions-3.0'\
    '/usr/local/lib/nautilus/extensions-2.0'\
    '/usr/lib64/nautilus/extensions-3.0'\
    '/usr/lib64/nautilus/extensions-2.0'\
    '/usr/lib/nautilus/extensions-3.0'\
    '/usr/lib/nautilus/extensions-2.0'\
    "$HOME/.nautilus/python-extensions"
do
  # check for $ONE_DIR/nautilusvim.py and remove them
  if [ -f "$ONE_DIR/nautilusvim.py" ]
  then
    INSTALLATION_FOUND=1

    rm -f "$ONE_DIR/nautilusvim.py" >/dev/null 2>&1
    
    if [ $? -ne 0 ]
    then
      echo "Unable to delete $ONE_DIR/nautilusvim.py."
    else
      echo "$ONE_DIR/nautilusvim.py is removed."
    fi
  fi
done

if [ $INSTALLATION_FOUND -eq 0 ]
then
  echo 'No nautilus-py-vim installation is found.'
fi

# vim73: cc=78
# vim: sw=2 ts=2 sts=2 tw=78 et
