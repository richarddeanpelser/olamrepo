import xmlrpc.client

class OL_manager:
   def __init__(self,user,pswd,url):
      self.url = url
      self.user = user
      self.pswd = pswd
      self.client = xmlrpc.client.ServerProxy(self.url)
      self.key = self.client.auth.login(self.user, self.pswd)
      
   def logout(self):   
      self.logout = self.client.auth.logout(self.key)

   def get_api_namespaces(self):
      api_call_list = self.client.api.getApiNamespaces(self.key)
      self.logout
      return api_call_list
   
   def get_name_space_methods(self, namespace):
      api_namespace_methods = self.client.api.getApiNamespaceCallList(self.key, namespace)
      self.logout
      return api_namespace_methods

   def get_all_systems(self):
      systems = self.client.system.listSystems(self.key)
      self.logout
      return systems
     
   def search_hostname(self, hostname):
      result = []
      systems = self.client.system.search.hostname(self.key, hostname)
      if not systems:
         print("No system found by that hostname")
      else:
         for system in systems:
               result.append(system['hostname'])
      self.logout
      return result

   def system_exists(self,hostname):
      systems = self.client.system.search.hostname(self.key, hostname)
      if not systems:
         exists = False
      else:
         if (len(systems) - 1) == 0 and str(systems[0]['hostname']).lower() == str(hostname).lower():
               exists = True
         else:
               exists = False
      self.logout
      return exists
   