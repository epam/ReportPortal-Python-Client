from requests import Session
from typing import Text, List
from reportportal_client.core.test_manager import TestManager

class RPClient:
    endpoint: Text = ...
    log_batch_size: int = ...
    project: Text = ...
    token: Text = ...
    launch_id: Text = ...
    verify_ssl: bool = ...
    is_skipped_an_issue: bool = ...
    api_v1: Text = ...
    api_v2: Text = ...
    base_url_v1: Text = ...
    base_url_v2: Text = ...
    session: Session = ...
    _test_manager: TestManager = ...

    def __init__(self, endpoint: Text, project: Text, token: Text,
                 log_batch_size: int = ...,
                 is_skipped_an_issue: bool = ..., verify_ssl: bool = ...,
                 retries: int = ...,
                 max_pool_size: int = ..., launch_id: Text = ...) -> None: ...

    def start_launch(self, name: Text, start_time: Text, description: Text = ...,
                     attributes: List = ..., mode: Text = ..., rerun: bool = ...,
                     rerun_of: Text = ..., **kwargs) -> Text: ...

    def finish_launch(self, end_time: Text, status: Text = ...,
                      attributes: List = ...,
                      **kwargs) -> dict: ...

    def start_item(self, name: Text, start_time: Text, item_type: Text,
                   description: Text = ...,
                   attributes: List = ..., parameters: dict = ...,
                   parent_item_id: Text = ..., has_stats: bool = ...,
                   code_ref: Text = ...,
                   **kwargs) -> Text: ...

    def finish_item(self, item_id: Text, end_time: Text, status: Text,
                    issue: Text = ...,
                    attributes: List = ..., **kwargs) -> None: ...

    def save_log(self, log_time, **kwargs) -> None: ...
