from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('gen_loc', INTEGER),
    Column('gen_type1', INTEGER),
    Column('gen_type2', INTEGER),
    Column('gen_type3', INTEGER),
    Column('subtype1', INTEGER),
    Column('subtype2', INTEGER),
    Column('subtype3', INTEGER),
    Column('subloc', INTEGER),
    Column('synopsis', VARCHAR(length=500)),
    Column('timestamp', DATETIME),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('gen_loc', Integer),
    Column('gen_type', Integer),
    Column('subtype', Integer),
    Column('subloc', Integer),
    Column('synopsis', String(length=500)),
    Column('timestamp', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['gen_type1'].drop()
    pre_meta.tables['event'].columns['gen_type2'].drop()
    pre_meta.tables['event'].columns['gen_type3'].drop()
    pre_meta.tables['event'].columns['subtype1'].drop()
    pre_meta.tables['event'].columns['subtype2'].drop()
    pre_meta.tables['event'].columns['subtype3'].drop()
    post_meta.tables['event'].columns['gen_type'].create()
    post_meta.tables['event'].columns['subtype'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['gen_type1'].create()
    pre_meta.tables['event'].columns['gen_type2'].create()
    pre_meta.tables['event'].columns['gen_type3'].create()
    pre_meta.tables['event'].columns['subtype1'].create()
    pre_meta.tables['event'].columns['subtype2'].create()
    pre_meta.tables['event'].columns['subtype3'].create()
    post_meta.tables['event'].columns['gen_type'].drop()
    post_meta.tables['event'].columns['subtype'].drop()
