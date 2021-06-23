"""Initial Migration

Revision ID: 7c16388a630b
Revises: 
Create Date: 2021-06-23 00:25:04.754593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c16388a630b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_title', sa.String(), nullable=True),
    sa.Column('post_content', sa.Text(), nullable=True),
    sa.Column('posted_at', sa.DateTime(), nullable=True),
    sa.Column('post_by', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###