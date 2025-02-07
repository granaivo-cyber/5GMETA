#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from __future__ import print_function

from proton.handlers import MessagingHandler
from proton.reactor import Container

import optparse
import json
import time
from proton.handlers import MessagingHandler
from proton.reactor import Container

#import address

import discovery_registration
from pygeotile.tile import Tile


import json
import codecs


latitude    = 43.2952
longitude    = -1.9850

tileTmp = Tile.for_latitude_longitude(latitude=latitude, longitude=longitude, zoom=18)
tile=str(tileTmp.quad_tree)
print(tile)
username="<username>"
password="<password>"

# Get Message Broker access
service="message-broker"
messageBroker_ip, messageBroker_port = discovery_registration.discover_sb_service(tile,service)
if messageBroker_ip == -1 or messageBroker_port == -1:
    print(service+" service not found")
    exit(-1)
    


url ="amqp://"+username+":"+password+"@"+messageBroker_ip+":"+str(messageBroker_port)+"/topic://event"


#url = 'amqp://<username>:<password>@192.168.10.9:5673/topic://events_5gmeta'

class Receiver(MessagingHandler):
    def __init__(self, url, messages_to_receive=10):
        super(Receiver, self).__init__()
        self.url = url
        self._messages_to_receive = messages_to_receive
        self._messages_actually_received = 0
        self._stopping = False

    def on_start(self, event):
        event.container.create_receiver(self.url)

    def on_message(self, event):
        if self._stopping:
            return

        print(event.message.body)
        msg=json.loads(event.message.body)
        print(msg['properties']['message'])
        #print(str(msg['payload']))
        #print(str(msg['payload']))
        #print(str(msg['payload']))
        #print(str(msg['payload']))
        #print(str(msg['payload']))
        self._messages_actually_received += 1
        if self._messages_actually_received == self._messages_to_receive:
            event.connection.close()
            self._stopping = True

    def on_transport_error(self, event):
        raise Exception(event.transport.condition)


if __name__ == "__main__":
    try:
        Container(Receiver(url)).run()
    except KeyboardInterrupt:
        pass
