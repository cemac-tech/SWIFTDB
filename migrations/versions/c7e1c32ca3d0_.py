"""empty message

Revision ID: c7e1c32ca3d0
Revises: 
Create Date: 2018-07-17 13:29:58.152019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7e1c32ca3d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partners',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('work_packages',
    sa.Column('wp_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('wp_id')
    )
    op.create_table('deliverables',
    sa.Column('deliverable_id', sa.String(), nullable=False),
    sa.Column('work_package', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('responsible_partner', sa.String(), nullable=False),
    sa.Column('month_due', sa.Integer(), nullable=True),
    sa.Column('progress', sa.String(), nullable=True),
    sa.Column('percent', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['responsible_partner'], ['partners.name'], ),
    sa.ForeignKeyConstraint(['work_package'], ['work_packages.wp_id'], ),
    sa.PrimaryKeyConstraint('deliverable_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deliverables')
    op.drop_table('work_packages')
    op.drop_table('partners')
    # ### end Alembic commands ###