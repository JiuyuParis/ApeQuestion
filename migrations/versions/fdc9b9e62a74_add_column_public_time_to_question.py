"""add column public_time to question

Revision ID: fdc9b9e62a74
Revises: d7d68eda7c67
Create Date: 2022-05-17 13:44:43.544032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdc9b9e62a74'
down_revision = 'd7d68eda7c67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('public_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'public_time')
    # ### end Alembic commands ###
