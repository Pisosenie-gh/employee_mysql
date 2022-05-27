"""Fix

Revision ID: 812bd280db59
Revises: bbfe8e21e7ac
Create Date: 2022-05-27 06:40:57.010848

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '812bd280db59'
down_revision = 'bbfe8e21e7ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('internal_employee', 'isActive',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Integer(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('internal_employee', 'isActive',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###