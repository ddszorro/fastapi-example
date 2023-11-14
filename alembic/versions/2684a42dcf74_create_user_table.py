"""create user table

Revision ID: 2684a42dcf74
Revises: 6714785fd3b0
Create Date: 2023-11-08 10:47:27.960457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, sql, ForeignKey
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = '2684a42dcf74'
down_revision: Union[str, None] = '6714785fd3b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True),
        sa.Column('password', sa.String(length=100), nullable=False),        
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))           
        
    )    
    pass


def downgrade() -> None:
    op.drop_table('users')    
    pass
