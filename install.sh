#!/bin/sh

# File: install.sh
#
# version 0.2
# by H Xu
#
# This is the install script for nautilus-py-vim.


INSTALL_DIRS=(\
  '/usr/lib64/nautilus/extensions-3.0/python' \
  '/usr/lib64/nautilus/extensions-2.0/python' \
  '/usr/lib/nautilus/extensions-3.0/python' \
  '/usr/lib/nautilus/extensions-2.0/python' \
  "$HOME/.nautilus/python-extensions" )

for ONE_INSTALL_DIR in ${INSTALL_DIRS[@]};
do
  # try to make the directory if not exist
  if [ ! -e $ONE_INSTALL_DIR ]
  then
    mkdir -p $ONE_INSTALL_DIR >/dev/null 2>&1 

    # if failed to create the directory, then let's turn to next directory in
    # the list
    if [ $? != 0 ]
    then
      continue
    fi
  fi

  # if we are able to write to the directory, try to copy nautilusvim.py to
  # it.
  if [ -d $ONE_INSTALL_DIR ] && [ -w $ONE_INSTALL_DIR ]
  then
    cp nautilusvim.py "$ONE_INSTALL_DIR/"

    echo "nautilus-py-vim has been successfully installed to $ONE_INSTALL_DIR"

    exit
  fi
done

# if we are here, the only reason is that the installation failed
echo "Failed to install nautilus-py-vim. You may try to install it manually."
echo "See README for more detailed."

# vim73: cc=78
# vim: ts=2 sw=2 et tw=78
