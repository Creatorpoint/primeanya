from . import start, admin, stats, group_events

def register_all_handlers(app):
    start.register(app)
    admin.register(app)
    stats.register(app)
    group_events.register(app)
