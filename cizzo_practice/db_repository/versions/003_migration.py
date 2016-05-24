from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('gen_loc', Integer),
    Column('gen_type1', Integer),
    Column('gen_type2', Integer),
    Column('gen_type3', Integer),
    Column('subtype1', Integer),
    Column('subtype2', Integer),
    Column('subtype3', Integer),
    Column('subloc', Integer),
    Column('synopsis', String(length=500)),
    Column('timestamp', DateTime),
)

event_subtype = Table('event_subtype', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('gen_type', Integer),
)

event_type = Table('event_type', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].create()
    post_meta.tables['event_subtype'].create()
    post_meta.tables['event_type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].drop()
    post_meta.tables['event_subtype'].drop()
    post_meta.tables['event_type'].drop()
