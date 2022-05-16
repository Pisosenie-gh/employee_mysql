"""Add military 

Revision ID: c9bbd3b41ba2
Revises: 48db8a3ce7a3
Create Date: 2022-04-18 11:26:56.519505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9bbd3b41ba2'
down_revision = '48db8a3ce7a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('military-service-attitude',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.Column('isActive', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_military-service-attitude_id'), 'military-service-attitude', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_military-service-attitude_id'), table_name='military-service-attitude')
    op.drop_table('military-service-attitude')
    # ### end Alembic commands ###