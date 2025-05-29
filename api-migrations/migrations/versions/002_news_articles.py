"""create news articles table

Revision ID: 002
Revises: 001
Create Date: 2024-04-02

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'news_articles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('excerpt', sa.Text(), nullable=False),
        sa.Column('author', sa.String(length=100), nullable=True),
        sa.Column('category', sa.String(length=50), nullable=True),
        sa.Column('image_base64', sa.Text(), nullable=True),
        sa.Column('published_date', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), onupdate=func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_articles_published_date'), 'news_articles', ['published_date'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_news_articles_published_date'), table_name='news_articles')
    op.drop_table('news_articles') 