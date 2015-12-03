import httplib

class Curl:
    def __init__(self, hostname="localhost", port=5000, debug=False, content_type="application/json"):
        self.hostname = hostname
        self.port = port
        self.debug = debug
        self.content_tp = content_type

    def __request__(self, tp, uri, param=""):
        if uri[0:2] == "//":
            uri = uri[1:]
        if uri[0] != "/":
            uri = "/" + uri
        headers = {'Content-type': self.content_tp, 'Accept': 'text/plain'}
        params = str(param).replace("'", "\"")
        conn = httplib.HTTPConnection(self.hostname, self.port)
        if self.debug:
            print "Request [" + tp + "][" + uri + "][" + params + "]"
        conn.request(tp, uri, params, headers)
        response = conn.getresponse()
        data = response.read()
        if self.debug:
            print "Response [" + str(response.status) + "][" + response.reason + "][" + data + "]"
        if response.status != 201:
            raise Exception("Error in " + tp.lower())
        return data

    def get(self, uri):
        return self.__request__("GET", uri)

    def post(self, uri, params):
        return self.__request__("POST", uri, params)

    def put(self, uri, params):
        return self.__request__("PUT", uri, params)

    def delete(self, uri, params):
        return self.__request__("DELETE", uri, params)
