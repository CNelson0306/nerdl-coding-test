"""create courses tables

Revision ID: 003
Revises: 002
Create Date: 2024-04-02

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic
revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None

def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('duration', sa.String(length=255), nullable=True),
        sa.Column('level', sa.String(length=255), nullable=True),
        sa.Column('section', sa.String(length=255), nullable=True),
        sa.Column('image_base64', sa.Text(), nullable=True),
        sa.Column('url', sa.String(length=2048), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), onupdate=func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.execute('INSERT INTO courses (title, description, duration, level, section) '
               'VALUES ("Test Title", "Test Description", "60 minutes", "Hard", "Section 1")')

def downgrade():
    op.drop_table('user_course_progress')
    op.drop_table('courses') 