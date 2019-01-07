"""empty message

Revision ID: 03225b07634c
Revises: bc915f504264
Create Date: 2019-01-03 10:29:17.903982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03225b07634c'
down_revision = 'bc915f504264'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deliverables', sa.Column('partner', sa.String(), nullable=False))
    op.drop_constraint('deliverables_responsible_partner_fkey', 'deliverables', type_='foreignkey')
    op.create_foreign_key(None, 'deliverables', 'partners', ['partner'], ['name'])
    op.drop_column('deliverables', 'responsible_partner')
    op.add_column('tasks', sa.Column('partner', sa.String(), nullable=False))
    op.drop_constraint('tasks_responsible_partner_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'partners', ['partner'], ['name'])
    op.drop_column('tasks', 'responsible_partner')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('responsible_partner', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_responsible_partner_fkey', 'tasks', 'partners', ['responsible_partner'], ['name'])
    op.drop_column('tasks', 'partner')
    op.add_column('deliverables', sa.Column('responsible_partner', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'deliverables', type_='foreignkey')
    op.create_foreign_key('deliverables_responsible_partner_fkey', 'deliverables', 'partners', ['responsible_partner'], ['name'])
    op.drop_column('deliverables', 'partner')
    # ### end Alembic commands ###
