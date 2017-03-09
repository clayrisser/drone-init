#!/usr/bin/env python2

import os
import os.path

def main():
    options = gather_information(get_defaults())
    if 'DRONE_SERVER' not in os.environ or 'DRONE_TOKEN' not in os.environ:
        setup_cli_access(
            drone_server=options['drone_server'],
            drone_token=options['drone_token']
        )
    repos = get_repos()
    secrets = get_secrets()
    add_secrets_to_repos(
        repos=repos,
        secrets=secrets
    )
    cleanup()

def get_defaults():
    return {
        'drone_server': 'https://example.com',
        'drone_token': 'my-drone-token'
    }

def gather_information(defaults):
    options = {}
    if 'DRONE_SERVER' in os.environ or 'DRONE_TOKEN' in os.environ:
        return options
    options['drone_server'] = _default_prompt('Drone Server', defaults['drone_server'])
    options['drone_token'] = _default_prompt('Drone Token', defaults['drone_token'])
    return options

def setup_cli_access(**kwargs):
    if os.path.isfile(os.environ['HOME'] + '/.bashrc'):
        path = os.environ['HOME'] + '/.bashrc'
        _append_to_file(path, '# Drone')
        _append_to_file(path, 'export DRONE_SERVER="' + kwargs['drone_server'] + '"')
        _append_to_file(path, 'export DRONE_TOKEN="' + kwargs['drone_token'] + '"')
    if os.path.isfile(os.environ['HOME'] + '/.zshrc'):
        path = os.environ['HOME'] + '/.zshrc'
        _append_to_file(path, '# Drone')
        _append_to_file(path, 'export DRONE_SERVER="' + kwargs['drone_server'] + '"')
        _append_to_file(path, 'export DRONE_TOKEN="' + kwargs['drone_token'] + '"')
    else:
        path = os.environ['HOME'] + '/.profile'
        _append_to_file(path, '# Drone')
        _append_to_file(path, 'export DRONE_SERVER="' + kwargs['drone_server'] + '"')
        _append_to_file(path, 'export DRONE_TOKEN="' + kwargs['drone_token'] + '"')

def get_repos(**kwargs):
    repos = kwargs['repos'] if 'repos' in kwargs else list()
    print('''
Create Repo
--------------------------------''')
    name = _default_prompt('Name', '')
    if name != '':
        repos.append(name)
        return get_repos(repos=repos)
    return repos

def get_secrets(**kwargs):
    secrets = kwargs['secrets'] if 'secrets' in kwargs else list()
    print('''
Add Secret
--------------------------------''')
    name = _default_prompt('Name', '')
    key = _default_prompt('Key', '')
    if name != '':
        secrets.append({
            'name': name,
            'key': key
        })
        return get_secrets(secrets=secrets)
    return secrets

def add_secrets_to_repos(**kwargs):
    for repo in kwargs['repos']:
        for secret in kwargs['secrets']:
            add_secret(
                repo=repo,
                secret=secret
            )
        print('''
''' + repo + '''
--------------------------------
        ''')
        os.system('drone secret ls ' + repo)

def add_secret(**kwargs):
    secret = kwargs['secret']
    os.system('drone secret add ' + kwargs['repo'] + ' ' + secret['name'] + ' ' + secret['key'])

def cleanup():
    if os.path.isfile(os.environ['HOME'] + '/.zshrc'):
        os.system('exec zsh -l')
    else:
        os.system('exec bash -l')

def _default_prompt(name, fallback):
    message = name + ': '
    if fallback != '':
        message = name + ' (' + fallback + '): '
    response = raw_input(message)
    assert isinstance(response, str)
    if (response):
        return response
    else:
        return fallback

def _append_to_file(path, content):
    with open(path, 'a') as f:
        f.write(content + '\n')

main()
