"""empty message

Revision ID: 98856d0a5e10
Revises: b73040b87f9a
Create Date: 2024-10-06 13:28:27.979617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98856d0a5e10'
down_revision: Union[str, None] = 'b73040b87f9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
