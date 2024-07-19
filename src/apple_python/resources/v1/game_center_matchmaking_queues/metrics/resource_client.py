"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import AsyncBaseClient, SyncBaseClient
from apple_python.resources.v1.game_center_matchmaking_queues.metrics.experiment_matchmaking_queue_sizes import (
    ExperimentMatchmakingQueueSizesClient,
    AsyncExperimentMatchmakingQueueSizesClient,
)
from apple_python.resources.v1.game_center_matchmaking_queues.metrics.experiment_matchmaking_requests import (
    AsyncExperimentMatchmakingRequestsClient,
    ExperimentMatchmakingRequestsClient,
)
from apple_python.resources.v1.game_center_matchmaking_queues.metrics.matchmaking_queue_sizes import (
    MatchmakingQueueSizesClient,
    AsyncMatchmakingQueueSizesClient,
)
from apple_python.resources.v1.game_center_matchmaking_queues.metrics.matchmaking_requests import (
    MatchmakingRequestsClient,
    AsyncMatchmakingRequestsClient,
)
from apple_python.resources.v1.game_center_matchmaking_queues.metrics.matchmaking_sessions import (
    AsyncMatchmakingSessionsClient,
    MatchmakingSessionsClient,
)


class MetricsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.experiment_matchmaking_queue_sizes = ExperimentMatchmakingQueueSizesClient(
            base_client=self._base_client
        )
        self.experiment_matchmaking_requests = ExperimentMatchmakingRequestsClient(
            base_client=self._base_client
        )
        self.matchmaking_queue_sizes = MatchmakingQueueSizesClient(
            base_client=self._base_client
        )
        self.matchmaking_requests = MatchmakingRequestsClient(
            base_client=self._base_client
        )
        self.matchmaking_sessions = MatchmakingSessionsClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)


class AsyncMetricsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.experiment_matchmaking_queue_sizes = (
            AsyncExperimentMatchmakingQueueSizesClient(base_client=self._base_client)
        )
        self.experiment_matchmaking_requests = AsyncExperimentMatchmakingRequestsClient(
            base_client=self._base_client
        )
        self.matchmaking_queue_sizes = AsyncMatchmakingQueueSizesClient(
            base_client=self._base_client
        )
        self.matchmaking_requests = AsyncMatchmakingRequestsClient(
            base_client=self._base_client
        )
        self.matchmaking_sessions = AsyncMatchmakingSessionsClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)