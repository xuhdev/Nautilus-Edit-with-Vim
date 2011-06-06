# File: nautilusvim.py
#
# version 0.3
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
        self.__read_conf_file()

    # read config file and set values
    def __read_conf_file(self):

        home_dir = os.getenv('HOME', '/');

        conf_file = None

        # search config files and set conf_file to the file path
        for a_file in [
                home_dir + '/.nautilusvim.conf',
                home_dir + '/.nautilus/nautilusvim.conf',
                '/etc/nautilusvim.conf']:
            if os.path.isfile(a_file) and os.access(a_file, os.R_OK):
                conf_file = a_file
                break

        # read the config file
        cf = ConfigParser.ConfigParser(False)

        # set default values
        cf.add_section('cmds')
        cf.set('cmds', 'gvim', 'gvim')
        cf.set('cmds', 'gvimdiff', 'gvim -d')
        cf.set('cmds', 'auth', 'gksu -k,beesu -m -c,kdesu -c')
        cf.add_section('prefs')
        # by default we don't fold menu items when right click on a single
        # file, but fold when right click on several files
        cf.set('prefs', 'fold_single', '0')
        cf.set('prefs', 'fold_multi', '1')

        # if we have found a config file, then load it
        if conf_file != None:
            cf.read(conf_file)

        self.gvim_cmd = cf.get('cmds', 'gvim')
        self.gvimdiff_cmd = cf.get('cmds', 'gvimdiff')
        self.auth_cmds = [cmd.strip()
                for cmd in cf.get('cmds', 'auth').split(',')]
        self.pref_fold_single = cf.getboolean('prefs', 'fold_single')
        self.pref_fold_multi = cf.getboolean('prefs', 'fold_multi')

    def __execute_as_root(self, cmd):
        # execute commands as root

        for auth_cmd in self.auth_cmds:
            try:
                os.system(auth_cmd + ' ' + cmd)
            except:
                continue
            else:
                return 0
        
        return 1

    #edit with single gvim
    def menu_activate_cb_single(self, menu, files):
        cmd_string = self.gvim_cmd
        for afile in files:
            cmd_string += " '" + afile.get_location().get_path() + "'"

        os.system(cmd_string)

    # edit with single gvim, root privilege
    def menu_activate_cb_single_root(self, menu, files):
        cmd_string = self.gvim_cmd
        for afile in files:
            cmd_string += " '" + afile.get_location().get_path() + "'"

        self.__execute_as_root(cmd_string)

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

            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_file_item_root',
                'Edit with gVim as root',
                'Edit with gVim Editor as root')
            new_item.connect('activate', self.menu_activate_cb_single_root,
                    files)
            items.append(new_item)

        elif len(files) > 1:
            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_single_file_item',
                'Edit with a Single gVim',
                'Edit with a Single gVim Editor')
            new_item.connect('activate', self.menu_activate_cb_single, files)
            items.append(new_item)

            new_item = nautilus.MenuItem(
                'NautilusPython::nautilusvim_single_file_item_root',
                'Edit with a Single gVim as root',
                'Edit with a Single gVim Editor as root')
            new_item.connect('activate', self.menu_activate_cb_single_root,
                    files)
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

        # if user choose to fold and sub menu item is supported, then set sub
        # menus
        if (((len(files) == 1 and self.pref_fold_single) or
                (len(files) > 1 and self.pref_fold_multi)) and
                hasattr(nautilus, 'Menu')):
            root_item = nautilus.MenuItem(
                    'NautilusPython::nautilusvim_root_item',
                    'NautilusVim',
                    'Nautilus extension for Vim')

            sub_menu = nautilus.Menu()
            root_item.set_submenu(sub_menu)
            for item in items:
                sub_menu.append_item(item)

            return [root_item]
        else:
            return items

# vim703: cc=78
# vim: et tw=78 sw=4 ts=4
