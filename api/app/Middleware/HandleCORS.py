import falcon
from falcon.http_status import HTTPStatus


class HandleCORS(object):
    def process_request(self, req, resp):
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')


