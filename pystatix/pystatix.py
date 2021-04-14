from os import stat
from sys import argv
from pwd import getpwuid
from time import ctime
from getopt import getopt, GetoptError


def version():

    print("+---------------------------------------------------------------------------------+")
    print("| Statix. Copyright (C) 2020 BrainDisassembly, Contact: braindisassm@gmail.com    |")
    print("| Version: 1.0.0                                                                  |")
    print("|                                                                                 |")
    print("| This program comes with ABSOLUTELY NO WARRANTY; for details type `show w`.      |")
    print("| This is free software, and you are welcome to redistribute it                   |")
    print("| under certain conditions; type `show c` for details.                            |")
    print("+---------------------------------------------------------------------------------+")


def usage():

    print("Usage: {0} --filename <options>".format(argv[0]))

    print("\nOptions:")
    print("  -h: --help                           Print usage and exit")
    print("  -V: --version                        Print version information and exit")
    print("  -f: --filename                       Filename")
    print("  -s: --byte-size                      Size of file, in bytes")
    print("  -p: --protection-bits                Protection bits")
    print("  -i: --inode-number                   Inode number")
    print("  -D: --device                         Device")
    print("  -H: --hard-links-number              Number of hard links")
    print("  -r: --recent-access                  Time of most recent access")
    print("  -M: --recent-modification            Time of most recent content modification")
    print("  -m: --metadata-change                Platform dependent; time of most recent metadata change on Unix")
    print("  -a: --allocated-blocks               Number of 512-byte blocks allocated for file")
    print("  -F: --filesystem-blocksize           Filesystem blocksize for efficient file system I/O")
    print("  -t: --type-of-device                 Type of device if an inode device")
    print("  -l: --login-name                     Login name")
    print("  -o: --optional-encrypted-password    Optional encrypted password")
    print("  -u: --user-id                        Numerical user ID")
    print("  -g: --group-id                       Numerical group ID")
    print("  -n: --name-field                     User name or comment field")
    print("  -d: --home-directory                 User home directory")
    print("  -I: --user-command-interpreter       User command interpreter")


def Statix():

    try:
        if filename:
            print('-- Filename: {0}'.format(filename))
        if byte_size:
            print('-- Size of file, in bytes: {0}'.format(stat(filename).st_size))
        if protection_bits:
            print('-- Protection bits: {0}'.format(stat(filename).st_mode))
        if inode_number:
            print('-- Inode number: {0}'.format(stat(filename).st_ino))
        if device:
            print('-- Device: {0}'.format(stat(filename).st_dev))
        if hard_links:
            print('-- Number of hard links: {0}'.format(stat(filename).st_nlink))
        if recent_access:
            print('-- Time of most recent access: {0}'.format(ctime(stat(filename).st_atime)))
        if recent_modification:
            print('-- Time of most recent content modification: {0}'.format(ctime(stat(filename).st_mtime)))
        if metadata_change:
            print('-- Platform dependent; time of most recent metadata change on Unix: {0}'.format(ctime(stat(filename).st_ctime)))
        if allocated_blocks:
            print('-- Number of 512-byte blocks allocated for file: {0}'.format(stat(filename).st_blocks))
        if filesystem_blocksize:
            print('-- Filesystem blocksize for efficient file system I/O: {0}'.format(stat(filename).st_blksize))
        if type_of_device:
            print('-- Type of device if an inode device: {0}'.format(stat(filename).st_rdev))
        if login_name:
            print('-- Login name: {0}'.format(getpwuid(stat(filename).st_uid).pw_name))
        if optional_encrypted_password:
            print('-- Optional encrypted password: {0}'.format(getpwuid(stat(filename).st_uid).pw_passwd))
        if user_id:
            print('-- Numerical user ID: {0}'.format(getpwuid(stat(filename).st_uid).pw_gid))
        if group_id:
            print('-- Numerical group ID: {0}'.format(getpwuid(stat(filename).st_uid).pw_uid))
        if name_field:
            print('-- User name or comment field: {0}'.format(getpwuid(stat(filename).st_uid).pw_gecos))
        if home_directory:
            print('-- User home directory: {0}'.format(getpwuid(stat(filename).st_uid).pw_dir))
        if user_command_interpreter:
            print('-- User command interpreter: {0}'.format(getpwuid(stat(filename).st_uid).pw_shell))

    except (OSError):
        print('-- {0}: No such file or directory'.format(filename))


def main():

    global filename
    filename_flag = False
    filename = ""

    global byte_size
    byte_size = ""

    global protection_bits
    protection_bits = ""

    global inode_number
    inode_number = ""

    global device
    device = ""

    global hard_links
    hard_links = ""

    global recent_access
    recent_access = ""

    global recent_modification
    recent_modification = ""

    global metadata_change
    metadata_change = ""

    global allocated_blocks
    allocated_blocks = ""

    global filesystem_blocksize
    filesystem_blocksize = ""

    global type_of_device
    type_of_device = ""

    global login_name
    login_name = ""

    global optional_encrypted_password
    optional_encrypted_password = ""

    global user_id
    user_id = ""

    global group_id
    group_id = ""

    global name_field
    name_field = ""

    global home_directory
    home_directory = ""

    global user_command_interpreter
    user_command_interpreter = ""

    try:
        opts, args = getopt(argv[1:], "hVf:spiDHrMmcaFtlougndI", ["help", "version", "filename=", "byte-size", "protection-bits", "inode-number", "device", "hard-links-number", "recent-access", "recent-modification", "metadata-change", "allocated-blocks", "filesystem-blocksize", "type-of-device", "login-name", "optional-encrypted-password", "user-id", "group-id", "name-field", "home-directory", "user-command-interpreter"])

    except GetoptError: usage()

    else:
        try:
            for opt, arg in opts:
                if opt in ("-h", "--help"): usage(); exit(1)
                if opt in ("-V", "--version"): version(); exit(1)
                if opt in ("-f", "--filename"): filename = arg; filename_flag = True
                if opt in ("-s", "--byte-size"): byte_size = True
                if opt in ("-p", "--protection-bits"): protection_bits = True
                if opt in ("-i", "--inode-number"): inode_number = True
                if opt in ("-D", "--device"): device = True
                if opt in ("-H", "--hard-links-number"): hard_links = True
                if opt in ("-r", "--recent-access"): recent_access = True
                if opt in ("-M", "--recent-modification"): recent_modification = True
                if opt in ("-m", "--metadata-change"): metadata_change = True
                if opt in ("-a", "--allocated-blocks"): allocated_blocks = True
                if opt in ("-F", "--filesystem-blocksize"): filesystem_blocksize = True
                if opt in ("-t", "--type-of-device"): type_of_device = True
                if opt in ("-l", "--login-name"): login_name = True
                if opt in ("-o", "--optional-encrypted-password"): optional_encrypted_password = True
                if opt in ("-u", "--user-id"): user_id = True
                if opt in ("-g", "--group-id"): group_id = True
                if opt in ("-n", "--name-field"): name_field = True
                if opt in ("-d", "--home-directory"): home_directory = True
                if opt in ("-I", "--user-command-interpreter"): user_command_interpreter = True

            if filename: Statix()

            elif byte_size: Statix(byte_size)
            elif protection_bits: Statix(protection_bits)
            elif inode_number: Statix(inode_number)
            elif device: Statix(device)
            elif hard_links: Statix(hard_links)
            elif recent_access: Statix(recent_access)
            elif recent_modification: Statix(recent_modification)
            elif metadata_change: Sstatix(metadata_change)
            elif allocated_blocks: Statix(allocated_blocks)
            elif filesystem_blocksize: Statix(filesystem_blocksize)
            elif type_of_device: Statix(type_of_device)
            elif login_name: Statix(login_name)
            elif optional_encrypted_password: Statix(iptional_encrypted_password)
            elif user_id: Statix(user_id)
            elif group_id: Statix(group_id)
            elif name_field: Statix(name_field)
            elif home_directory: Statix(home_directory)
            elif user_command_interpreter: Statix(user_command_interpreter)

            else:
                usage()

        except (UnboundLocalError):
            pass
    
        except (TypeError):
            pass

if __name__ == "__main__":
        main()
