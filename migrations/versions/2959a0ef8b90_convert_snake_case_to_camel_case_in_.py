"""convert snake_case to camel_case in message table

Revision ID: 2959a0ef8b90
Revises: e2238e5d76c9
Create Date: 2021-10-19 18:51:37.556207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2959a0ef8b90'
down_revision = 'e2238e5d76c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('userId', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('companyId', sa.Integer(), nullable=True))
    op.drop_constraint('messages_user_id_fkey', 'messages', type_='foreignkey')
    op.drop_constraint('messages_company_id_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['userId'], ['id'])
    op.create_foreign_key(None, 'messages', 'companies', ['companyId'], ['id'])
    op.drop_column('messages', 'user_id')
    op.drop_column('messages', 'company_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('company_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_company_id_fkey', 'messages', 'companies', ['company_id'], ['id'])
    op.create_foreign_key('messages_user_id_fkey', 'messages', 'users', ['user_id'], ['id'])
    op.drop_column('messages', 'companyId')
    op.drop_column('messages', 'userId')
    # ### end Alembic commands ###
