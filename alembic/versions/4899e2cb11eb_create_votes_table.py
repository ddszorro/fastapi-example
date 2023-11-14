"""create votes table

Revision ID: 4899e2cb11eb
Revises: 0590f9e783db
Create Date: 2023-11-08 10:48:57.803910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, sql, ForeignKey
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = '4899e2cb11eb'
down_revision: Union[str, None] = '0590f9e783db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "votes",
        sa.Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    )
    pass


def downgrade() -> None:
    op.drop_table('votes')        
    pass
