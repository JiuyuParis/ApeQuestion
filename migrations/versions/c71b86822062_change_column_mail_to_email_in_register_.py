"""change column mail to email in register_capture

Revision ID: c71b86822062
Revises: af04886a0e95
Create Date: 2022-05-15 21:18:09.465350

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c71b86822062'
down_revision = 'af04886a0e95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('register_capture', sa.Column('email', sa.String(length=100), nullable=False))
    op.drop_index('mail', table_name='register_capture')
    op.create_unique_constraint(None, 'register_capture', ['email'])
    op.drop_column('register_capture', 'mail')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('register_capture', sa.Column('mail', mysql.VARCHAR(collation='utf8_croatian_ci', length=100), nullable=False))
    op.drop_constraint(None, 'register_capture', type_='unique')
    op.create_index('mail', 'register_capture', ['mail'], unique=False)
    op.drop_column('register_capture', 'email')
    # ### end Alembic commands ###