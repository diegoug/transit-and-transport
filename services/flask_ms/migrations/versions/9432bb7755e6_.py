"""empty message

Revision ID: 9432bb7755e6
Revises: 
Create Date: 2023-02-27 03:45:45.242344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9432bb7755e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('officials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('identification_number', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('identification_number')
    )
    op.create_table('persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('license_plate', sa.String(length=10), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['persons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('infractions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('comments', sa.String(length=255), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.Column('official_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['official_id'], ['officials.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('infractions')
    op.drop_table('vehicles')
    op.drop_table('persons')
    op.drop_table('officials')
    # ### end Alembic commands ###
