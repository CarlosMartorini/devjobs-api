"""empty message

Revision ID: 0d78f67736d3
Revises: 38a5ae1ac0fc
Create Date: 2021-10-13 18:10:14.059014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d78f67736d3'
down_revision = '38a5ae1ac0fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('degree', sa.String(length=255), nullable=False),
    sa.Column('school', sa.String(length=255), nullable=False),
    sa.Column('date_from', sa.Date(), nullable=True),
    sa.Column('date_to', sa.Date(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('education')
    # ### end Alembic commands ###