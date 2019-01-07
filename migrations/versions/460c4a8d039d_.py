"""empty message

Revision ID: 460c4a8d039d
Revises: 03225b07634c
Create Date: 2019-01-07 13:56:13.683601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '460c4a8d039d'
down_revision = '03225b07634c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('work_packages', sa.Column('issues', sa.String(), nullable=True))
    op.add_column('work_packages', sa.Column('next_deliverable', sa.String(), nullable=True))
    op.alter_column('work_packages', 'status',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('work_packages', 'status',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('work_packages', 'next_deliverable')
    op.drop_column('work_packages', 'issues')
    # ### end Alembic commands ###
