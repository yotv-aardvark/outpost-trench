import inngest

from core.workflows.client import inngest_client


@inngest_client.create_function(
    fn_id="hello.world",
    # event that triggers this function
    trigger=inngest.TriggerEvent(event="app/hello.world"),
)
async def hello_world(ctx: inngest.Context) -> str:
    ctx.logger.info(ctx.event)
    return "done"
