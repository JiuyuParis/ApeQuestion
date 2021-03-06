"""add column email to user

Revision ID: 969a37097e71
Revises: b5ca8c9d6001
Create Date: 2022-05-16 11:35:55.853804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '969a37097e71'
down_revision = 'b5ca8c9d6001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
