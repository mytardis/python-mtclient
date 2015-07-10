import requests
import six
from six.moves.urllib.parse import urlunsplit


class MTClient(object):

    def __init__(self, host, secure=True, version=None):
        self.use_async = six.PY3
        self.host = host
        self.scheme = 'https' if secure else 'http'
        if version is None:
            self.version = 'v1'

    def _build_url(self, action=None, query=None):
        path = '/api/{version}/'.format(version=self.version)
        if action is not None:
            path = '{path}/{action}/'.format(prefix=path,
                                             action=action)
        return urlunsplit((self.scheme,
                           self.host,
                           path,
                           query,
                           ''))

    def request(self, action=None, method='GET', payload=None):
        return requests.get(self._build_url(action))

    def get_server_version(self):
        try:
            import ipdb; ipdb.set_trace()
            response = self.request()
        except requests.RequestException:
            return None
        return response
