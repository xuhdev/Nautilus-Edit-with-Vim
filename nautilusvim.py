# File: nautilusvim.py
#
# version 0.2.1
# by H Xu
#
# This file is the major part of nautilus-py-vim.


import os
import nautilus
import gconf
import ConfigParser


class NautilusVimExtension(nautilus.MenuProvider):

    def __init__(self):
        self.client = gconf.client_get_default()
        self.read_conf_file()

    # read config file and set values
    def read_conf_file(self):

        # first set default value
        self.gvim_cmd = 'gvim'
        self.gvimdiff_cmd = 'gvim -d'

        home_dir = os.getenv('HOME', '/');

        conf_file = None

        # search config files and set conf_file to the file path
        for a_file in [
                home_dir + '/.nautilusvim.conf',
                home_dir + '/.nautilus/.nautilusvim.conf',
                '/etc/nautilusvim.conf']:
            if os.path.isfile(a_file) and os.access(a_file, os.R_OK):
                conf_file = a_file
                break

        if conf_file == None:
            return

        # read the config file
        cf = ConfigParser.ConfigParser(False)

        cf.read(conf_file)

        tmpval = cf.get('cmds', 'gvim')
        if tmpval != None:
            self.gvim_cmd = tmpval

        tmpval = cf.get('cmds', 'gvimdiff')
        if tmpval != None:
            self.gvimdiff_cmd = tmpval


    #edit with single gvim
    def menu_activate_cb_single(self, menu, files):
        cmd_string = self.gvim_cmd
        for afile in files:
            cmd_string += " '" + afile.get_location().get_path() + "'"

        os.system(cmd_string)

    # edit with mutli gvim
    def menu_activate_cb_multi(self, menu, files):
        for afile in files:
            os.system(self.gvim_cmd + " '" +
                    afile.get_location().get_path() + "'")

    # diff with gvim
    def menu_activate_cb_diff(self, menu, files):
        cmd_string = self.gvimdiff_cmd
        for afile in files:
            cmd_string += " '" + afile.get_location().get_path() + "'"
        
        os.system(cmd_string)

    def get_file_items(self, window, files):
        items = []

        if len(files) == 1:
            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_file_item',
                'Edit with gVim',
                'Edit with gVim Editor')
            new_item.connect('activate', self.menu_activate_cb_single, files)
            items.append(new_item)

        elif len(files) > 1:
            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_single_file_item',
                'Edit with a Single gVim',
                'Edit with a Single gVim Editor')
            new_item.connect('activate', self.menu_activate_cb_single, files)
            items.append(new_item)

            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_multi_file_item',
                'Edit with Multi gVim',
                'Edit with Mutli gVim Editors')
            new_item.connect('activate', self.menu_activate_cb_multi, files)
            items.append(new_item)

            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_diff_file_item',
                'Diff with gVim',
                'Diff with gVim')
            new_item.connect('activate', self.menu_activate_cb_diff, files)
            items.append(new_item)


        return items

# vim703: cc=78
# vim: et tw=78 sw=4 ts=4
