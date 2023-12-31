"""empty message

Revision ID: 0c1a25490d05
Revises: 6216aa0b5bfc
Create Date: 2023-09-05 21:53:20.771339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c1a25490d05'
down_revision = '6216aa0b5bfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('whiskey', schema=None) as batch_op:
        batch_op.alter_column('brand',
               existing_type=sa.VARCHAR(length=5),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('whiskey', schema=None) as batch_op:
        batch_op.alter_column('brand',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=5),
               existing_nullable=False)

    # ### end Alembic commands ###
