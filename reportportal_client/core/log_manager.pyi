from logging import Logger
from requests import Session
from threading import Lock

from six.moves import queue

from reportportal_client.core.rp_requests import (
    HttpRequest as HttpRequest,
    RPFile as RPFile,
    RPLogBatch as RPLogBatch,
    RPRequestLog as RPRequestLog
)
from reportportal_client.core.worker import APIWorker as APIWorker
from typing import Any, Dict, List, Optional, Text

logger: Logger

class LogManager:
    _lock: Lock = ...
    _log_endpoint: Text = ...
    _logs_batch: List = ...
    _worker: APIWorker = ...
    api_version: Text = ...
    command_queue: queue.Queue = ...
    data_queue: queue.PriorityQueue = ...
    launch_id: Text = ...
    log_batch_size: int = ...
    project_name: Text = ...
    rp_url: Text = ...
    session: Session = ...
    verify_ssl: bool = ...
    def __init__(self,
                 rp_url: Text,
                 session: Session,
                 api_version: Text,
                 launch_id: Text,
                 project_name: Text,
                 log_batch_size: int = ...,
                 verify_ssl: bool = ...) -> None: ...

    def _log_process(self, log_req: RPRequestLog) -> None: ...
    def _send_batch(self) -> None: ...
    def log(self,
            time: Text,
            message: Optional[Text] = ...,
            level: Optional[Text] = ...,
            attachment: Optional[Dict] = ...,
            item_id: Optional[Text] = ...) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def stop_force(self) -> None: ...
