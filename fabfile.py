

def git_pull():
    "Updates the repository."
    run("cd ~/git/$(repo)/; git pull $(parent) $(branch)")

def git_reset():
    "Resets the repository to specified version."
    run("cd ~/git/$(repo)/; git reset --hard $(hash)")

def production():
    config.fab_hosts = ['a.example.com', 'b.example.com']
    config.repos = (('project',, 'origin', 'master'),
                    ('app', 'origin', 'master'))

def staging():
    config.fab_hosts = ['a.staging_example.com', 'b.staging_example.com']
    config.repos = (("project", 'origin', 'master'),
                    ('app', 'origin', 'master'))


def reboot():
    "Reboot Apache server"
    sudo("apache2ctl graceful")

def pull():
    require('fab_hosts', provided_by=[production])
    for repo, parent, branch in config_repos:
        config.repo = repo
        config.parent = parent
        config.branch = branch
        invoke(git_pull)

def reset(repo, hash):
    require("fab_hosts", provided_by=[staging, production])
    config.hash = hash
    config.repo = repo
    invoke(git_reset)

