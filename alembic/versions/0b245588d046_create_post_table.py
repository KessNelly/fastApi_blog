"""create post table

Revision ID: 0b245588d046
Revises: 
Create Date: 2024-07-22 10:48:16.928938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b245588d046'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


#def upgrade() -> None:
def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


#def downgrade() -> None:
def downgrade():
    op.drop_table('posts')
    pass
