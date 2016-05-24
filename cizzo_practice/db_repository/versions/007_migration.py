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

event_subtype = Table('event_subtype', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('gen_type', INTEGER),
)

event_type = Table('event_type', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
)

sub_loc = Table('sub_loc', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('gen_loc', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].drop()
    pre_meta.tables['event_subtype'].drop()
    pre_meta.tables['event_type'].drop()
    pre_meta.tables['sub_loc'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].create()
    pre_meta.tables['event_subtype'].create()
    pre_meta.tables['event_type'].create()
    pre_meta.tables['sub_loc'].create()
