from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# Revision identifiers
revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None

def upgrade():
    connection = op.get_bind()

    connection.execute(
        sa.text("""
                INSERT INTO news_articles (title, excerpt, author, category, image_base64, published_date)
                VALUES
                (
                    :title1, :excerpt1, :author1, :category1, :image1, :published1
                ),
                (
                    :title2, :excerpt2, :author2, :category2, :image2, :published2
                ),
                (
                    :title3, :excerpt3, :author3, :category3, :image3, :published3
                ),
                (
                    :title4, :excerpt4, :author4, :category4, :image4, :published4
                ),
            """),
            {
                "title1": "Breaking News: Falcon Takes Off",
                "excerpt1": "Falcon framework simplifies web APIs.",
                "author1": "Jane Doe",
                "category1": "Tech",
                "image1": None,
                "published1": 2025,

                "title2": "React Leads The Way",
                "excerpt2": "Why React is being used by so many employers.",
                "author2": "Bob",
                "category2": "Development",
                "image2": None,
                "published2": 2025,

                "title3": "Engineering Solutions Driving Results",
                "excerpt3": "Tech company specialising in building scalable software solutions.",
                "author3": "John Doe",
                "category3": "Business",
                "image3": None,
                "published3": 2025,

                "title4": "Blockchain Solutions Driving Real-World Impact",
                "excerpt4": "Cryto giants building secure, scalable blockchain infrastructure",
                "author4": "Sue Doe",
                "image4": None,
                "published4": 2025
            }
    )

def downgrade():
    op.drop_table('articles') 

    



                
    
