import falcon
from falcon_cors import CORS

from Middleware.HandleCORS import HandleCORS

from Resources.HealthCheck import HealthCheckResource
from Resources.Courses import Courses

# Import the news articles class
from Resources.NewsArticles import NewsArticles


# Middleware
cors_middleware = HandleCORS()

cors = CORS(
    allow_all_origins=True,
    allow_all_headers=True,
    allow_all_methods=True,
    allow_credentials_all_origins=True,
    expose_headers_list=['*']
)

# Create the Falcon application with middleware
app = falcon.App(middleware=[
    cors.middleware,
])


# Resources
healthcheck = HealthCheckResource()
courses = Courses()



# Routes
# Healthcheck
app.add_route('/healthz', healthcheck)

# Courses
app.add_route('/public/courses', courses)
app.add_route('/public/courses/{course_id}', courses)


# News Article

news_articles = NewsArticles()

app.add_route('/public/articles', news_articles)
app.add_route('/public/articles{article_id}', news_articles)

