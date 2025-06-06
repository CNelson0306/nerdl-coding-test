from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# Imported datetime to use for published date
import datetime

# Revision identifiers
revision = '005'
down_revision = '004'
branch_labels = None
depends_on = None

def upgrade():
    connection = op.get_bind()

    articles = [
            {
                "title": "Breaking News: Falcon Takes Off",
                "excerpt": "Falcon framework simplifies web APIs.",
                "author": "Jane Doe",
                "category": "Tech",
                "image_base64": None,
                "published_date": datetime.date(2025, 1, 1)
            },
            {
                "title": "React Leads The Way",
                "excerpt": "Why React is being used by so many employers.",
                "author": "Bob",
                "category": "Development",
                "image_base64": None,
                "published_date": datetime.date(2025, 1, 1)
            },
            {
                "title": "Solutions Driving Results",
                "excerpt": "Tech company specialising in building scalable software solutions.",
                "author": "John Doe",
                "category": "Business",
                "image_base64": None,
                "published_date": datetime.date(2025, 1, 1)
            },
            {
                "title": "Blockchain Solutions",
                "excerpt": "Crypto giants building secure, scalable blockchain infrastructure.",
                "author": "Sue Doe",
                "category": "Crypto",
                "image_base64": None,
                "published_date": datetime.date(2025, 1, 1)
            }
        ]

    connection.execute(
        sa.text("""
            INSERT INTO news_articles (title, excerpt, author, category, image_base64, published_date)
            VALUES (:title, :excerpt, :author, :category, :image_base64, :published_date)
        """),
        articles
    )

def downgrade():
    connection = op.get_bind()
    connection.execute(sa.text("DELETE FROM news_articles WHERE author IN ('Jane Doe', 'Bob', 'John Doe', 'Sue Doe')"))

    




                
    
