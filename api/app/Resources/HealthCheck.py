import falcon
from datetime import datetime

class HealthCheckResource:
    def on_get(self, req, resp):
        """Health check endpoint that returns service status and timestamp."""
        health_info = {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "service": "falcon-api"
        }
        resp.status = falcon.HTTP_200
        resp.media = health_info 