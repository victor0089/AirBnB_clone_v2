#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""

from datetime import datetime
from fabric.api import env, local, put, run
import os

env.hosts = ["54.144.152.30", "35.174.176.12"]


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    local("mkdir -p versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(current_time)
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """

    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive
        put(archive_path, "/tmp/")

        # Create the release directory
        release_dir = "/data/web_static/releases/{}".format(
            os.path.basename(archive_path).replace(".tgz", "")
        )
        run("mkdir -p {}".format(release_dir))

        # Unpack the archive
        run("tar -xzf /tmp/{} -C {}/".format(
            os.path.basename(archive_path), release_dir
        ))

        # Move contents to proper location
        run("mv {}/web_static/* {}/".format(release_dir, release_dir))

        # Remove unnecessary directory
        run("rm -rf {}/web_static".format(release_dir))

        # Delete the symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Deploys the archive to the web servers
    """

    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
