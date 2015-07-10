import json
import unittest
import requests
import requests_mock

import mtclient


class BasicsTestCase(unittest.TestCase):

    @requests_mock.Mocker(kw='req_mock')
    def setUp(self, req_mock):
        self.basic_response = {
            "datafileparameter": {
                "list_endpoint": "/api/v1/datafileparameter/",
                "schema": "/api/v1/datafileparameter/schema/"},
            "datafileparameterset": {
                "list_endpoint": "/api/v1/datafileparameterset/",
                "schema": "/api/v1/datafileparameterset/schema/"},
            "dataset": {"list_endpoint": "/api/v1/dataset/",
                        "schema": "/api/v1/dataset/schema/"},
            "dataset_file": {"list_endpoint": "/api/v1/dataset_file/",
                             "schema": "/api/v1/dataset_file/schema/"},
            "datasetparameter": {
                "list_endpoint": "/api/v1/datasetparameter/",
                "schema": "/api/v1/datasetparameter/schema/"},
            "datasetparameterset": {
                "list_endpoint": "/api/v1/datasetparameterset/",
                "schema": "/api/v1/datasetparameterset/schema/"},
            "experiment": {"list_endpoint": "/api/v1/experiment/",
                           "schema": "/api/v1/experiment/schema/"},
            "experimentparameter": {
                "list_endpoint": "/api/v1/experimentparameter/",
                "schema": "/api/v1/experimentparameter/schema/"},
            "experimentparameterset": {
                "list_endpoint": "/api/v1/experimentparameterset/",
                "schema": "/api/v1/experimentparameterset/schema/"},
            "facility": {"list_endpoint": "/api/v1/facility/",
                         "schema": "/api/v1/facility/schema/"},
            "group": {"list_endpoint": "/api/v1/group/",
                      "schema": "/api/v1/group/schema/"},
            "instrument": {"list_endpoint": "/api/v1/instrument/",
                           "schema": "/api/v1/instrument/schema/"},
            "location": {"list_endpoint": "/api/v1/location/",
                         "schema": "/api/v1/location/schema/"},
            "objectacl": {"list_endpoint": "/api/v1/objectacl/",
                          "schema": "/api/v1/objectacl/schema/"},
            "parametername": {"list_endpoint": "/api/v1/parametername/",
                              "schema": "/api/v1/parametername/schema/"},
            "replica": {"list_endpoint": "/api/v1/replica/",
                        "schema": "/api/v1/replica/schema/"},
            "schema": {"list_endpoint": "/api/v1/schema/",
                       "schema": "/api/v1/schema/schema/"},
            "storagebox": {"list_endpoint": "/api/v1/storagebox/",
                           "schema": "/api/v1/storagebox/schema/"},
            "storageboxattribute": {
                "list_endpoint": "/api/v1/storageboxattribute/",
                "schema": "/api/v1/storageboxattribute/schema/"},
            "storageboxoption": {"list_endpoint": "/api/v1/storageboxoption/",
                                 "schema": "/api/v1/storageboxoption/schema/"},
            "user": {"list_endpoint": "/api/v1/user/",
                     "schema": "/api/v1/user/schema/"}}

        req_mock.register_uri('GET',
                              'http://mytardis.com/api/v1/',
                              text=json.dumps(self.basic_response))
        self.client = mtclient.MTClient(host='mytardis.com',
                                        secure=False)

    def tearDown(self):
        pass

    @requests_mock.Mocker(kw='req_mock')
    def test_mocking(self, req_mock):
        mocking_response = {'mocked': 'you'}
        req_mock.register_uri('GET', 'http://test.com',
                              text=json.dumps(mocking_response))
        self.assertEqual(requests.get('http://test.com').json(),
                         mocking_response)

    def test_version_check(self):
        self.assertEqual(self.client.get_server_version(), '1')
