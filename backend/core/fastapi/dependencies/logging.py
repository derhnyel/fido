from fastapi import BackgroundTasks


class Logging:
    """
    Logging dependency.
    Args:
        background_task: Send log as Backgroud task.
    """

    def __init__(self, background_task: BackgroundTasks) -> None:
        background_task.add_task(self._send_log)

    async def _send_log(self) -> None:
        """
        Send log.
        """
        

