from flask import make_response
from flask_restful import Api
from werkzeug.wrappers import Response


from handlers.rag_engine import (
    RagEngineResource,
    TestResource,
    TestViewResource
)

from handlers.base import org_scoped_rule



class ApiExt(Api):
    def add_org_resource(self, resource, *urls, **kwargs):
        urls = [org_scoped_rule(url) for url in urls]
        return self.add_resource(resource, *urls, **kwargs)


api = ApiExt()

api.add_org_resource(RagEngineResource, "/api/rag_engine", endpoint="rag_engine")
api.add_org_resource(TestResource, "/api/test", endpoint="test")
api.add_org_resource(TestViewResource, "/api/view", endpoint="view")
