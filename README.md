# Nautilus-Edit-with-Vim

## Overview

Nautilus-Edit-with-Vim is an extension for nautilus, the GNOME file manager,
and is written in python. This extension adds several menu items in the
nautilus right-click context menu for gvim, just like gVim on Windows.

## Install

To install this extension, first make sure that you have installed the
[nautilus python extension](http://projects.gnome.org/nautilus-python):

    $ # On Fedora
    $ sudo yum install nautilus-python

    $ # On Debian/Ubuntu
    $ sudo apt-get install python-nautilus

If you want to enable the "Edit with gVim as Root" menu item, you should
install [gksu](http://www.nongnu.org/gksu),
[beesu](http://honeybeenet.altervista.org/beesu) or
[kdesu](http://techbase.kde.org/Projects/kdesu):

    $ # On Fedora:
    $ sudo yum install beesu

    $ # On Debian/Ubuntu
    $ sudo apt-get install gksu

After that, run the following command to install in user directory:

    $ curl -L http://github.com/xuhdev/nautilus-edit-with-vim/raw/master/nautilusvim.py >~/.local/share/nautilus-python/extensions/nautilusvim.py

Or to install system-widely:

    # curl -L http://github.com/xuhdev/nautilus-edit-with-vim/raw/master/nautilusvim.py >$XDG_DATA_DIR/share/nautilus-python/extensions/nautilusvim.py

Then restart nautilus(execute "nautilus -q") and try to right click on the
file(s) you want to edit, you will see the changes in the context menu("Edit
with gVim" when only one file is selected, and "Diff with gVim", "Edit with
Multi gVim", "Edit with a Single gVim" are present when several files are
selected), just like what it is like on Windows.

## Configuration

To configure the extension, you could write a config file. Nautilus-Edit-with-Vim
will search the config file in the order of the following files:

- ~/.nautilusvim.conf
- ~/.nautilus/nautilusvim.conf
- /etc/nautilusvim.conf

For the content of the config file, you could take a look at the
[example.conf][].

If none of the configuration files are found, Nautilus-Edit-with-Vim will use
default values.

## Uninstall

Remove user's local installation:

    rm ~/.local/share/nautilus-python/extensions/nautilusvim.py

Remove a system-wide installation:

    rm $XDG_DATA_DIR/share/nautilus-python/extensions/nautilusvim.py



[example.conf]: https://github.com/xuhdev/nautilus-edit-with-vim/blob/master/example.conf
