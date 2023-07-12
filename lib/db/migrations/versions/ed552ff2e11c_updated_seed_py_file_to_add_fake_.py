"""updated seed.py file to add fake arrival time

Revision ID: ed552ff2e11c
Revises: bd68f6d826d8
Create Date: 2023-07-12 15:27:25.332844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed552ff2e11c'
down_revision = 'bd68f6d826d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('confirmation', sa.String(), nullable=True))
    op.add_column('reservations', sa.Column('reservation_status', sa.String(), nullable=True))
    op.add_column('reservations', sa.Column('date', sa.DateTime(), nullable=True))
    op.alter_column('reservations', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.create_foreign_key(None, 'reservations', 'flights', ['flight_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reservations', type_='foreignkey')
    op.alter_column('reservations', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_column('reservations', 'date')
    op.drop_column('reservations', 'reservation_status')
    op.drop_column('reservations', 'confirmation')
    # ### end Alembic commands ###
