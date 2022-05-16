"""Add marital

Revision ID: 4a5725bfb3e8
Revises: 9e6b1f699dee
Create Date: 2022-04-18 11:51:27.492834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a5725bfb3e8'
down_revision = '9e6b1f699dee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nationality-gender', sa.Column('isActive', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('nationality-gender', 'isActive')
    # ### end Alembic commands ###
