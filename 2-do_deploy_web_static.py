#!/usr/bin/python3
"""
Module: 2-do_deploy_web_static.py
Function to deploy web_static archive to web servers.
"""

from fabric.api import env, put, run
import os

env.hosts = ['<IP_WEB_01>', '<IP_WEB_02>']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Args:
        archive_path (str): Path to the archive on the local machine.

    Returns:
        bool: True if all operations have been done correctly, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)          # web_static_20240610231825.tgz
        folder_name = filename.replace(".tgz", "")         # web_static_20240610231825

        # Upload archive to remote /tmp/
        put(archive_path, "/tmp/{}".format(filename))

        # Create release folder
        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))

        # Uncompress archive
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, folder_name))

        # Remove archive
        run("rm /tmp/{}".format(filename))

        # Move contents out of nested web_static
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(folder_name, folder_name))

        # Remove redundant web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder_name))

        # Delete current symlink
        run("rm -rf /data/web_static/current")

        # Create new symlink
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error:", e)
        return False
