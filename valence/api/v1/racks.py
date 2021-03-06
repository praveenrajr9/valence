# Copyright (c) 2016 Intel, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from flask import request
import flask_restful
from six.moves import http_client

from valence.common import utils
from valence.redfish import redfish

LOG = logging.getLogger(__name__)


class RackList(flask_restful.Resource):

    def get(self):
        return utils.make_response(
            http_client.OK, redfish.list_racks(request.get_json()))


class Rack(flask_restful.Resource):

    def get(self, rack_id):
        return utils.make_response(
            http_client.OK, redfish.show_rack(rack_id))
