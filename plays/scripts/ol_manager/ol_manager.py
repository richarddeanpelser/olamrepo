#!/usr/bin/env python3
from OLM_API import OL_manager
import arguments

if __name__== "__main__":

   username = arguments.args.username
   password= arguments.args.password
   api_url= arguments.args.api_url

   olm = OL_manager(
      arguments.args.username,
      arguments.args.password,
      arguments.args.api_url
      )

   if arguments.args.get_call_list:
      call_list = olm.get_api_namespaces()
      for call in call_list:
         print(call)

   if arguments.args.all_systems:
      systems = olm.get_all_systems()
      for system in systems:
         print(system['name'])
         
   if arguments.args.hostname:
      hosts = olm.search_hostname(arguments.args.hostname)
      for host in hosts:
         print(host)

   if arguments.args.verify:
      print(olm.system_exists(arguments.args.verify))

   if arguments.args.namespace_methods:
      methods = olm.get_name_space_methods(arguments.args.namespace_methods)
      for method in methods:
         print(method)
