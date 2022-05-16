# About This Repo #
This is a skeleton of an Ansible home directory. You can control all of your application environments from this directory. If you work with multiple customers, you probably want to create a separate copy of this repo for each customer.

This repo was designed to help new Ansible users to get up and running quickly. Feel free to add to it and add additional tips and tricks. Pull requests welcome.

This repo includes a docker compose template for quick and easy testing of your ansible projects

# customizations:

I used [mattjbarlow/ansible-directory](https://github.com/mattjbarlow/ansible-directory) as a start but made the following changes
I didn't produce a pull request against his repo as this one deviates from it significantly.

* [handle playbooks in subdirectories.](https://github.com/ansible/ansible/issues/12862)
* Puth host_vars and group_vars in a separate inventory subdirectory
* exclusively use yaml / yml files for inventory, variables. <br/>
  There is now a consistent use of yaml through out this ansible directory template
* separate sub directory for community roles <br/>
  [best-practices-to-build-great-ansible-playbooks](https://blog.theodo.fr/2015/10/best-practices-to-build-great-ansible-playbooks/)
* include a local ansible.cfg file to override defaults. <br/>
  In order for all these changes to work <br/>
  * set roles dir so play books work from subdirectory
  * set pipelining on by default for newer host
* Set python3 as default <br/>
  This also sets the default python version as a group variable for use on newer hosts that run python version3 by default
* Set some simple hello world feed back in the template tasks and playbooks
* added examples of how to use ansible commands
* added docker compose to install latest ubuntu LTS with Openssl to test you ansible code against <br/>
  This should work on linux and windows with out many changes <br/>
  Assumes you have docker / docker compose installed and working on your machine <br/>
  This is used to check your plays work and config is set correctly. <br/>
  This is not used to deploy dockrized environments. <br/>
  [vagrant-docker-and-ansible-wtf](http://devo.ps/blog/vagrant-docker-and-ansible-wtf/)

## inspired by

[https://blog.newrelic.com/engineering/ansible-best-practices-guide/](https://blog.newrelic.com/engineering/ansible-best-practices-guide/) <br/>
[https://github.com/ansible/ansible/issues/12862](https://github.com/ansible/ansible/issues/12862) <br/>
[https://leucos.github.io/ansible-files-layout](https://leucos.github.io/ansible-files-layout) <br/>
[https://github.com/ansible/ansible-examples](https://github.com/ansible/ansible-examples) <br/>
[https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html) <br/>
[https://blog.theodo.fr/2015/10/best-practices-to-build-great-ansible-playbooks/](https://blog.theodo.fr/2015/10/best-practices-to-build-great-ansible-playbooks/) <br/>
[http://devo.ps/blog/vagrant-docker-and-ansible-wtf/](http://devo.ps/blog/vagrant-docker-and-ansible-wtf/) <br/>

## Ansible Tips #

## Using plays in a subdirectory

Get [docker compose](docker/README.md) up and running

```
cd /tmp/
git clone https://github.com/nelaaro/ansible-directory.git
# or
git clone https://github.com/nelaaro/ansible-directory.git your-ansilbe-project-name
cd ./your-ansilbe-project-name

# run test play book
ansible-playbook ./site.yml -l local -i ./inventory/staging.yml -u root

# run test play book in subdir
ansible-playbook ./plays/test-play.yml -l local -i ./inventory/staging.yml -u root
```

## Ansible roles
In your roles directory, type ansible-galaxy init <em>role_name</em> in order to generate an empty skeleton for a new role you are working on.

Example:
<pre>
cd ./roles/community
ansible-galaxy init nginx
</pre>

Check out [Ansible Examples](https://github.com/ansible/ansible-examples) for example playbooks.

# My Directory Layout #

Based on [Ansible Best Practices](https://docs.ansible.com/ansible/playbooks_best_practices.html#directory-layout)

<pre>
inventory
   production.yml         # inventory file for production servers
   staging.yml            # inventory file for staging environment

   group_vars
      all.yml             # all.yml so you can gloably set variables for all groups
      group1.yml          # here we assign variables to particular groups
      group2.yml          # ""
   host_vars
      hostname1.yml       # if systems need specific variables, put them here
      hostname2.yml       # ""

library/                  # if any custom modules, put them here (optional)
filter_plugins/           # if any custom filter plugins, put them here (optional)

plays
   webservers.yml         # playbook for webserver tier
   dbservers.yml          # playbook for dbserver tier
site.yml                  # master playbook

roles/
    community
        ansible-galaxy-play
    common/               # this hierarchy represents a "role"
        tasks/            #
            main.yml      #  <-- tasks file can include smaller files if warranted
        handlers/         #
            main.yml      #  <-- handlers file
        templates/        #  <-- files for use with the template resource
            ntp.conf.j2   #  <------- templates end in .j2
        files/            #
            bar.txt       #  <-- files for use with the copy resource
            foo.sh        #  <-- script files for use with the script resource
        vars/             #
            main.yml      #  <-- variables associated with this role
        defaults/         #
            main.yml      #  <-- default lower priority variables for this role
        meta/             #
            main.yml      #  <-- role dependencies

    webtier/              # same kind of structure as "common" was above, done for the webtier role
    monitoring/           # ""
    fooapp/               # ""

ansible.cfg               # Override some defaults so this directory structure will work from any where
</pre>

# olamrepo
