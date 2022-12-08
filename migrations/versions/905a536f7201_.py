"""empty message

Revision ID: 905a536f7201
Revises: fb6f1c17731e
Create Date: 2022-12-07 23:43:39.481273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '905a536f7201'
down_revision = 'fb6f1c17731e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reset_password_uuid', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('reset_password_uuid')

    # ### end Alembic commands ###