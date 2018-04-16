#!/usr/bin/python
import ipaddress
class FilterModule(object):
    def filters(self):
        return {
            "net_addr_wmask_filter": self.net_addr_wmask_filter,
            "ipaddr_womask_filter": self.ipaddr_womask_filter
        }

    def net_addr_wmask_filter(self, ipaddr_wmask):
        interface = ipaddress.ip_interface(ipaddr_wmask)
        return interface.network.with_prefixlen

    def ipaddr_womask_filter(self, ipaddr_wmask):
        interface = ipaddress.ip_interface(ipaddr_wmask)
        return interface.ip
