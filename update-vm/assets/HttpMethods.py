import requests
from colorama import Fore, Style
from requests.auth import HTTPBasicAuth

class HTTPError(Exception):
    """Excepción personalizada para errores."""
    pass

class HTTPMethods:
    def __init__(self):
        self.vm_api = 'https://vcd.clarocloud.com/api/vApp/'

    def custom_hardware(self, username, password, token, api_version):
        headersPost = {
            'Accept': f'application/*+xml;version={api_version}',
            'Content-Type': 'application/vnd.vmware.vcloud.rasdItem+xml',
            'x-vcloud-authorization': token
        }
        
        # Los datos a modificar (RAM y CPU) se obtienen de hacer :
        # GET /vApp/{id}/virtualHardwareSection/memory
        # GET /vApp/{id}/virtualHardwareSection/cpu
        
        #Body para modificar RAM
        body = """
        <ns2:Item xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1" xmlns:ns2="http://www.vmware.com/vcloud/v1.5" xmlns:vmext="http://www.vmware.com/vcloud/extension/v1.5" xmlns:vssd="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_VirtualSystemSettingData" xmlns:common="http://schemas.dmtf.org/wbem/wscim/1/common" xmlns:rasd="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_ResourceAllocationSettingData" xmlns:vmw="http://www.vmware.com/schema/ovf" xmlns:ovfenv="http://schemas.dmtf.org/ovf/environment/1" xmlns:ns9="http://www.vmware.com/vcloud/versions" ns2:type="application/vnd.vmware.vcloud.rasdItem+xml" ns2:href="https://vcd.clarocloud.com/api/vApp/{id}/virtualHardwareSection/memory">
            <rasd:Address xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:AddressOnParent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:AllocationUnits>byte * 2^20</rasd:AllocationUnits>
            <rasd:AutomaticAllocation xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:AutomaticDeallocation xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:ConfigurationName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:ConsumerVisibility xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:Description>Memory Size</rasd:Description>
            <rasd:ElementName>4096 MB of memory</rasd:ElementName>
            <rasd:Generation xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:InstanceID>5</rasd:InstanceID>
            <rasd:Limit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:MappingBehavior xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:OtherResourceType xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:Parent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:PoolID xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:Reservation>0</rasd:Reservation>
            <rasd:ResourceSubType xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:ResourceType>4</rasd:ResourceType>
            <rasd:VirtualQuantity>4096</rasd:VirtualQuantity>
            <rasd:VirtualQuantityUnits xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            <rasd:Weight>0</rasd:Weight>
            <ns2:Link rel="edit" href="https://vcd.clarocloud.com/api/vApp/{id}/virtualHardwareSection/memory" type="application/vnd.vmware.vcloud.rasdItem+xml"/>
            <ns2:Link rel="edit" href="https://vcd.clarocloud.com/api/vApp/{id}/virtualHardwareSection/memory" type="application/vnd.vmware.vcloud.rasdItem+json"/>
        </ns2:Item>
        """
        custom_ram = f'{self.vm_api}/{id}/virtualHardwareSection/memory'
        # custom_cpu = f'{self.vm_api}/{id}/virtualHardwareSection/cpu'
        
        auth = HTTPBasicAuth(username, password)
        response = requests.put(custom_ram, auth=auth, headers=headersPost, data=body) 

        if(response.status_code == 202):
            response = response.text
            print(f"{Fore.GREEN}[Success]{Style.RESET_ALL} VM actualizada con éxito.")   

        return response
        
# Escribir output en un archivo
# with open('example_cpu_xml.txt', 'w') as file:     
#     file.write(response.text)
#     file.write('\n\n')
