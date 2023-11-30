from fabric import task
from invoke import run as local

remote_path = "/home/natebeaty/apps/rafikihandyman"
remote_hosts = ["natebeaty@natebeaty.com"]
git_branch = "main"
php_command = "php82"

# set to production
# @task
# def production(c):
#     global remote_hosts, remote_path
#     remote_hosts = ["natebeaty@natebeaty.com"]
#     remote_path = "/home/natebeaty/apps/rafikihandyman"
#     git_branch = "main"

# deploy
@task(hosts=remote_hosts)
def deploy(c):
    update(c)
    composer_update(c)
    build(c)
    clear_cache(c)

def update(c):
    c.run("cd {} && git pull origin {}".format(remote_path, git_branch))

def composer_update(c):
    c.run("cd {} && {} ~/bin/composer.phar install  --no-interaction --prefer-dist --optimize-autoloader --no-dev".format(remote_path, php_command))

def build(c):
    c.run("cd {} && npm ci")
    c.run("cd {} && npm run build")
    c.run("cd {} && {} artisan cache:clear".format(remote_path, php_command))
    c.run("cd {} && {} artisan config:cache".format(remote_path, php_command))
    c.run("cd {} && {} artisan route:cache".format(remote_path, php_command))
    c.run("cd {} && {} artisan statamic:stache:warm".format(remote_path, php_command))
    c.run("cd {} && {} artisan queue:restart".format(remote_path, php_command))
    c.run("cd {} && {} artisan statamic:search:update --all".format(remote_path, php_command))

def clear_cache(c):
    c.run("cd {} && {} artisan statamic:static:clear".format(remote_path, php_command))
    c.run("cd {} && {} artisan statamic:static:warm --queue".format(remote_path, php_command))

# local commands
# @task
# def assets(c):
#     local("npx run build")
