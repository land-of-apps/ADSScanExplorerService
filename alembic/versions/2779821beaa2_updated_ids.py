"""Updated ids

Revision ID: 2779821beaa2
Revises: 35b8136d4902
Create Date: 2022-06-17 10:15:18.328756

"""
from enum import unique
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '2779821beaa2'
down_revision = 'f47027cc246c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('page2article_article_id_fkey', 'page2article', type_='foreignkey')
    op.drop_constraint('page2article_page_id_fkey', 'page2article', type_='foreignkey')
    op.drop_constraint('article_collection_id_fkey', 'article', type_='foreignkey')
    op.drop_constraint('page_collection_id_fkey', 'page', type_='foreignkey')
    op.alter_column('article', 'bibcode',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('article', 'collection_id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('article', 'id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('collection', 'id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('page', 'id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('page', 'collection_id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('page2article', 'page_id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('page2article', 'article_id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.String(),
               existing_nullable=False)
    op.create_unique_constraint(None, 'article', ['bibcode'])
    op.create_foreign_key(None, 'page2article', 'article', ['article_id'], ['bibcode'])
    op.create_foreign_key(None, 'page2article', 'page', ['page_id'], ['id'])
    op.create_foreign_key(None, 'article', 'collection', ['collection_id'], ['id'])
    op.create_foreign_key(None, 'page', 'collection', ['collection_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('page2article_article_id_fkey', 'page2article', type_='foreignkey')
    op.drop_constraint('page2article_page_id_fkey', 'page2article', type_='foreignkey')
    op.drop_constraint('article_collection_id_fkey', 'article', type_='foreignkey')
    op.drop_constraint('page_collection_id_fkey', 'page', type_='foreignkey')
    # op.drop_constraint(None, 'page2article', type_='foreignkey')
    # op.create_foreign_key('page2article_article_id_fkey', 'page2article', 'article', ['article_id'], ['id'])
    op.drop_column('page2article', 'article_id')
    op.add_column('page2article', sa.Column('article_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    op.drop_column('page2article', 'page_id')
    op.add_column('page2article', sa.Column('page_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    op.drop_column('page', 'collection_id')
    op.add_column('page', sa.Column('collection_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    op.drop_column('page', 'id')
    op.add_column('page', sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    op.drop_column('collection', 'id')
    op.add_column('collection', sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    op.drop_column('article', 'id')
    op.add_column('article', sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    op.drop_column('article', 'collection_id')
    op.add_column('article', sa.Column('collection_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True))
    
    op.create_unique_constraint('collection_id_uniq', 'collection', ['id'])
    op.create_unique_constraint(None, 'article', ['id'])
    op.create_unique_constraint('page_id_uniq', 'page', ['id'])

    op.create_index('article_volume_index', 'article', ['collection_id'], unique=False)
    op.create_index('page_volume_index', 'page', ['collection_id'], unique=False)

    op.create_foreign_key(None, 'page2article', 'article', ['article_id'], ['id'])
    op.create_foreign_key(None, 'page2article', 'page', ['page_id'], ['id'])
    op.create_foreign_key(None, 'article', 'collection', ['collection_id'], ['id'])
    op.create_foreign_key(None, 'page', 'collection', ['collection_id'], ['id'])
    # ### end Alembic commands ###
