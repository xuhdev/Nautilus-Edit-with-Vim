#!/bin/sh

# File: install.sh
#
# version 0.3
# by H Xu
#
# This is the install script for nautilus-edit-with-vim.


for ONE_INSTALL_DIR in\
  "$XDG_DATA_DIR/share/nautilus-python/extensions" \
  "$HOME/.local/share/nautilus-python/extensions" \
do

  # make the "$HOME/.nautilus/python-extensions" before we check it
  if [ $ONE_INSTALL_DIR = "$HOME/.local/share/nautilus-python/extensions" ]
  then
    mkdir -p "$ONE_INSTALL_DIR" >/dev/null 2>&1
  fi

  # if we are able to write to the directory, try to copy nautilusvim.py to
  # it.
  if [ -d $ONE_INSTALL_DIR ] && [ -w $ONE_INSTALL_DIR ]
  then
    cp nautilusvim.py "$ONE_INSTALL_DIR/"

    echo "nautilus-py-vim has been successfully installed to $ONE_INSTALL_DIR"
    echo "Restart nautilus to complete the installation."

    exit
  fi
done

# if we are here, the only reason is that the installation failed
echo "Failed to install nautilus-py-vim. You may try to install it manually"
echo "by copying nautilusvim.py to ~/.nautilus/python-extensions/ and then"\
  "restart nautilus."

# vim73: cc=78
# vim: ts=2 sw=2 et tw=78
