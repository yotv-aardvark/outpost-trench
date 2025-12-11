import datetime

import inngest

from core.workflows.client import inngest_client


@inngest_client.create_function(
    fn_id="sync-systems",
    # A Function is triggered by events
    trigger=inngest.TriggerEvent(event="auto/sync.request"),
    # Easily add Throttling with Flow Control
    throttle=inngest.Throttle(
        limit=2, period=datetime.timedelta(minutes=1)
    ),
)
def sync_systems(ctx: inngest.ContextSync) -> None:
    # step is retried if it throws an error
    data = ctx.step.run("Get data", lambda: print("step is running"))

    # Steps can reuse data from previous ones
    # ctx.step.run("Save data", db.syncs.insert_one, data)
