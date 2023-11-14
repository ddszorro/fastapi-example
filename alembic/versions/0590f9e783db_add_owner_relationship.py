"""add owner relationship

Revision ID: 0590f9e783db
Revises: 2684a42dcf74
Create Date: 2023-11-08 10:48:35.006055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, sql, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision: str = '0590f9e783db'
down_revision: Union[str, None] = '2684a42dcf74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", Integer, ForeignKey("users.id", ondelete="CASCADE")))
    # op.add_column("posts", sa.Column("owner", relationship("User")))
    pass

def downgrade() -> None:
    op.drop_column("posts","owner_id")
    # op.drop_column("posts", "owner")
    pass
