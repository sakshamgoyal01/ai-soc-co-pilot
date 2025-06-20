import ansible_runner

def run_playbook(playbook_path, extra_vars={}):
    r = ansible_runner.run(private_data_dir=".", playbook=playbook_path, extravars=extra_vars)
    return r.status