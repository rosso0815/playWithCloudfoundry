#! /usr/bin/env python3

import os
from cloudfoundry_client.client import CloudFoundryClient

target_endpoint = 'https://api.dev.cfdev.sh'
proxy = dict(http=os.environ.get('HTTP_PROXY', ''),
             https=os.environ.get('HTTPS_PROXY', ''))

# print('1')
client = CloudFoundryClient(target_endpoint, verify=False)
# print('1.5')
# init with user credentials
client.init_with_user_credentials('user', 'pass')
# print('2')
# init with refresh token (that will retrieve a fresh access token)
# client.init_with_token('refresh-token')
# init with access and refresh token (if the above method is not convenient)
#client.refresh_token = 'refresh-token'
#client._access_token = 'access-token'
# print('3')
print('#--- organization ---#')
for organization in client.v2.organizations:
    print(organization['metadata']['guid'])
print('#--- ---#')
