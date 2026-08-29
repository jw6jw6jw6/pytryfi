"""No-op stand-ins for the sentry_sdk helpers pytryfi calls.

Upstream calls sentry_sdk.init() with a DSN owned by the library author.
sentry_sdk's default logging integration hooks the root logger, so that captures
every ERROR record in the *host* application, not just pytryfi's. This fork drops
the dependency. These shims keep the upstream call sites untouched so the diff
stays small and rebases cleanly.
"""


def capture_exception(*args, **kwargs):
    return None


def capture_message(*args, **kwargs):
    return None
