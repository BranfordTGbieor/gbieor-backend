"""init migration

Revision ID: f1d2b3dc84ee
Revises: 
Create Date: 2024-01-10 10:56:35.623706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1d2b3dc84ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=150), nullable=True),
    sa.Column('lastname', sa.String(length=150), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('usertype', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('photo', sa.String(length=150), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_timestamp'), ['timestamp'], unique=False)

    op.create_table('blog',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('blog_title', sa.String(length=200), nullable=True),
    sa.Column('headline_image', sa.String(length=100), nullable=True),
    sa.Column('blog_body', sa.String(length=500), nullable=True),
    sa.Column('blog_image_one', sa.String(length=100), nullable=True),
    sa.Column('blog_image_two', sa.String(length=100), nullable=True),
    sa.Column('blog_image_three', sa.String(length=100), nullable=True),
    sa.Column('blog_image_four', sa.String(length=100), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_blog_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_blog_timestamp'), ['timestamp'], unique=False)

    op.create_table('subscribe',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('subscribed', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('subscribe', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_subscribe_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_subscribe_timestamp'), ['timestamp'], unique=False)

    op.create_table('comment',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('blog_id', sa.BigInteger(), nullable=True),
    sa.Column('user_comment', sa.String(length=250), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_comment_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_comment_timestamp'))
        batch_op.drop_index(batch_op.f('ix_comment_id'))

    op.drop_table('comment')
    with op.batch_alter_table('subscribe', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_subscribe_timestamp'))
        batch_op.drop_index(batch_op.f('ix_subscribe_id'))

    op.drop_table('subscribe')
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_blog_timestamp'))
        batch_op.drop_index(batch_op.f('ix_blog_id'))

    op.drop_table('blog')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_timestamp'))
        batch_op.drop_index(batch_op.f('ix_user_id'))

    op.drop_table('user')
    # ### end Alembic commands ###
