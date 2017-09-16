#!/usr/bin/python
# -*- coding: utf-8 -*-

# [..] various imports

# this line must be written exactly that way,
# as Ansible will replace it with the "imported" code
from ansible.module_utils.basic import *

# [..] implementation code omitted

# simplified, flat version of the actual code
if __name__ == '__main__':
    global module
    module = AnsibleModule(
        argument_spec={
            'name': {'required': True, 'type': 'str'}
        },
        supports_check_mode=False
    )

    args = module.params
    # [..] check for early return reasons
    module.exit_json(changed=False, msg="Hello " + args['name'])
