#!/usr/bin/python3
"""
Fabric script to deploy a web_static archive locally
"""

from datetime import datetime
from fabric.api import local, run, put
import os

# Set local host for testing
env.hosts = ['localhost']

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    local("mkdir -p versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(current_time)

    # Create or copy required files to web_static directory
    local("echo '<html><body>Content of 0-index.html</body></html>' > web_static/0-index.html")
    local("echo '<html><body>This is my custom index page</body></html>' > web_static/my_index.html")

    # Create the archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    return archive_path

def do_deploy(archive_path):
    """
    Deploys an archive locally
    """

    if not os.path.exists(archive_path):
        return False

    try:
        # Create the release directory
        release_dir = "data/web_static/releases/{}".format(
            os.path.basename(archive_path).replace(".tgz", "")
        )

        local("mkdir -p {}".format(release_dir))

        # Unpack the archive
        local("tar -xzf {} -C {}/".format(
            archive_path, release_dir
        ))

        # Move contents to proper location
        local("mv {}/web_static/* {}/".format(release_dir, release_dir))

        # Remove unnecessary directory
        local("rm -rf {}/web_static".format(release_dir))

        # Delete the symbolic link
        local("rm -rf data/web_static/current")

        # Create a new symbolic link
        local("ln -s {} data/web_static/current".format(release_dir))

        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False

def deploy():
    """
    Deploys the archive locally
    """

    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()
