#import log_utils

import json
import urllib3
import urllib

PUT_METHOD = 'PUT'
GET_METHOD = 'GET'
POST_METHOD = 'POST'
DELETE_METHOD = 'DELETE'

TEXT_XML_HTTP_HEADER = {'Content-Type': 'text/xml'}
JSON_HTTP_HEADER = {'Content-Type': 'application/json'}    

def urljoin(*args):
    return '/'.join(arg.strip('/') for arg in args if isinstance(arg, basestring))

class RequestsManager(object):
    """This class represent the Stash server we are going to interact with
       default_url will be: hostname:port/default_url_postfix"""
    def __init__(self, hostname, port, default_url_postfix=None, credentials=None, proxy=None):
        self.pool = None
        self.default_headers = dict()
        ##self.logger = log_utils.get_logger(return_valid_filename(hostname))

        if proxy is None:
            self.pool = urllib3.PoolManager()
        else:
            self.pool = urllib3.ProxyManager(proxy)


        self.hostname = hostname
        self.port = port
        self.default_url = "%s:%s" % (self.hostname, self.port)

        if default_url_postfix is not None:
            self.default_url += default_url_postfix

        if credentials is not None:
            self.default_headers = urllib3.util.make_headers(basic_auth=credentials)

        #self.logger.debug("Starting pool. hostname=%s, port=%s, default_url=%s, default_headers=%s, proxy=%s" % (self.hostname, self.port, self.default_url, self.default_headers, proxy))

    def send_request(self, method, url_postfix="", headers=dict(), fields=None, output_file=None):
        url = self._generate_url(url_postfix)
        headers = self._generate_headers(headers)
        #self.logger.debug("Sending request. method=%s, url=%s, headers=%s, fields=%s" % (method, url, headers, fields))
        reply = self.pool.request(method, url, fields=fields, headers=headers).data
        self._log_reply(reply)

        if output_file is not None and reply is not None:
            pass
            #self.logger.debug('Saving reply to file. output_file=%s' % (output_file))

        return reply

    def urlopen(self, method, url_postfix="", headers=dict(), body=None):
        url = self._generate_url(url_postfix)
        headers = self._generate_headers(headers)
        #self.logger.debug("Sending urlopen request. method=%s, url=%s, headers=%s, body=%s" % (method, url, headers, body))        
        reply = self.pool.urlopen(method, (self.default_url + url_postfix), body=body, headers=dict(self.default_headers.items() + headers.items())).data
        self._log_reply(reply)
        return reply

    def _log_reply(self, reply):
        pass
        #self.logger.debug('received reply[0:100]:\n%s' % (reply[0:100] if len(reply) > 100 else reply))

    def _generate_url(self, url_postfix):
        return self.default_url + url_postfix

    def _generate_headers(self, headers):
        return  dict(self.default_headers.items() + headers.items())

def download_url(url):
    return urllib.urlopen(url).read()