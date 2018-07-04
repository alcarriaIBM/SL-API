"""
Create a new Virtual Guest.
createObject() enables the creation of computing instances on an account.
This method is a simplified alternative to interacting with the ordering
system directly.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import sys

# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = '3044554_angel.alcarria.nieto@es.ibm.com'

# Generate one at https://control.softlayer.com/account/users
API_KEY = sys.argv[1]

orderToRequest = {
    "datacenter": {
        "name": "ams01"
        },
    "dedicatedAccountHostOnlyFlag": "false",
    "domain": "test.local",
    "hostname": "test",
    "hourlyBillingFlag": "true",
    "localDiskFlag": "false",
    "maxMemory": "1024",
    "networkComponents": [
        {
          "maxSpeed": 100
        }
      ],
    "operatingSystemReferenceCode": "CENTOS_LATEST",
    "startCpus": "1"
    }

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)
productOrderService = client['SoftLayer_Product_Order']


"""
To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
when you are ready to create the server call the createObject method instead.
"""
try:

    newOrder = client['Virtual_Guest'].verifyOrder(orderToRequest)
    pp(newOrder)
    # response = productOrderService.verifyOrder(orderData)


except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to create a new Virtual Guest faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))
