"""
Controller to interface with BBC iPlayer.
"""

# Note: Media ID is NOT the 8 digit alpha-numeric in the URL
# it can be found by right clicking the playing video on the web interface
# e.g. https://www.bbc.co.uk/iplayer/episode/b09w7fd9/bitz-bob-series-1-1-castle-makeover shows:
# "2908kbps | dash (mf_cloudfront_dash_https)
#  b09w70r2 | 960x540"

import logging
from typing import Any

from ..config import APP_BBCIPLAYER
from .media import STREAM_TYPE_BUFFERED, STREAM_TYPE_LIVE, BaseMediaPlayer

APP_NAMESPACE = "urn:x-cast:com.google.cast.media"


class BbcIplayerController(BaseMediaPlayer):
    """Controller to interact with BBC iPlayer namespace."""

    def __init__(self) -> None:
        super().__init__(APP_BBCIPLAYER)
        self.logger = logging.getLogger(__name__)

    def quick_play(
        self,
        *,
        media_id: str,
        timeout: float,
        is_live: bool = False,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        """Quick Play helper for BBC iPlayer media."""
        stream_type = STREAM_TYPE_LIVE if is_live else STREAM_TYPE_BUFFERED
        metadata_default = {"metadataType": 0, "title": ""}
        if metadata is None:
            metadata = metadata_default
        subtitle = metadata.pop("subtitle", "")

        super().quick_play(
            media_id=media_id,
            media_type=None,
            stream_type=stream_type,
            metadata=metadata,
            media_info={"customData": {"secondary_title": subtitle}},
            timeout=timeout,
            **kwargs,
        )
