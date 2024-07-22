"""add content column to posts table

Revision ID: 6a0f31e27fa2
Revises: 0b245588d046
Create Date: 2024-07-22 11:27:21.003149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a0f31e27fa2'
down_revision: Union[str, None] = '0b245588d046'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
#def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
#def downgrade():
    op.drop_column('posts', 'content')
    pass
