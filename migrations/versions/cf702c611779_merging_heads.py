"""merging heads

Revision ID: cf702c611779
Revises: 0f9babdfe259, 16974fe99d3e, d287014843c0
Create Date: 2021-10-14 14:00:01.455339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf702c611779'
down_revision = ('0f9babdfe259', '16974fe99d3e', 'd287014843c0')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
