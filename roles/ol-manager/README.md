Role Name
=========

ol-manager

Requirements
------------

This role requires connection details and credentials for the Oracle linux Manager server.
We currently use a custom credential type in OLAM(AWX) that injects the username, password,
and URL during playbook execution. 

These credentials are seperate to the ones required to register clients with Oracle Linux Manager.
They are used by the python script in tasks/scripts/ol_manager.py. 

Failure to run successfully connect to the Oracle Linux Manager server prior to registering systems will result
in failure. This to prevent duplicate system from being added.

Role Variables
--------------
The following varables are injected by custom credentials in AWX to the get_existing_systems.yml task located in tasks/get_existing_systems.yml

olm_username
olm_password
olm_url

If you need an alternative way to pass variables store them in the vars files of the role or create host variables in the top level project. Make sure you encrypt variable files containing passwords.


Dependencies
------------
No depencies required for installation.



Example Playbook
----------------

- name: test-play.yml apply common configuration to all nodes
  hosts: all
  user: root
  

  roles:
    - ol-manager



Author Information
------------------

Richard-Dean Pelser