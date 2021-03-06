"""empty message

Revision ID: 51bd435bd5cc
Revises: e831a883153a
Create Date: 2021-03-06 18:05:34.252719

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51bd435bd5cc'
down_revision = 'e831a883153a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alias', sa.Column('transfer_token', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'alias', ['transfer_token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'alias', type_='unique')
    op.drop_column('alias', 'transfer_token')
    # ### end Alembic commands ###
