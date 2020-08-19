#!/usr/bin/python3
""" deploy with fabric of static files of aribnb
"""

from fabric.api import *
from os import path

env.hosts = ['34.75.26.100', '	35.237.221.251']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases'
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        directory = archive.split('.')
        run("sudo mkdir -p {}/{}/".format(path, directory[0]))
        run("sudo tar -xzf /tmp/{} -C {}/{}/".format(archive,
                                                     path,
                                                     directory[0]))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv {}/{}/web_static/* {}/{}/".format(path, directory[0],
                                                       path, directory[0]))
        run("sudo rm -rf {}/{}/web_static".format(path, directory[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{}/ /data/web_static/current".format(path,
                                                                 directory[0]))
        print("New version deployed!")
        return True
    except:
        return False