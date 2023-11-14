"""create post table

Revision ID: 6714785fd3b0
Revises: 
Create Date: 2023-11-08 10:16:16.194784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, sql, ForeignKey
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = '6714785fd3b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=45), nullable=False),
        sa.Column('content', sa.String(length=500), nullable=False),
        sa.Column('published', sa.Boolean, server_default=sql.false(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))     
        )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
