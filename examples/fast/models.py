import sqlalchemy
from sqlalchemy.types import JSON

metadata = sqlalchemy.MetaData()

zoom_webhook_event_table = sqlalchemy.Table(
    'zoom_webhook_events',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("event", sqlalchemy.String(40)),
    sqlalchemy.Column("event_ts", sqlalchemy.BigInteger),
    sqlalchemy.Column("payload", JSON),
)
