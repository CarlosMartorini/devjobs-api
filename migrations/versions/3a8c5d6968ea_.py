"""empty message

Revision ID: 3a8c5d6968ea
Revises: 0d78f67736d3
Create Date: 2021-10-13 18:19:00.395626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a8c5d6968ea'
down_revision = '0d78f67736d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'education', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'education', type_='foreignkey')
    # ### end Alembic commands ###