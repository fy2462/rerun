# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/video_frame_reference.fbs".

# You can extend this class by creating a "VideoFrameReferenceExt" class in "video_frame_reference_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components, datatypes
from .._baseclasses import (
    Archetype,
)
from ..error_utils import catch_and_log_exceptions
from .video_frame_reference_ext import VideoFrameReferenceExt

__all__ = ["VideoFrameReference"]


@define(str=False, repr=False, init=False)
class VideoFrameReference(VideoFrameReferenceExt, Archetype):
    """
    **Archetype**: References a single video frame.

    Used to display individual video frames from a [`archetypes.AssetVideo`][rerun.archetypes.AssetVideo].
    To show an entire video, a video frame reference for each frame of the video should be logged.

    See <https://rerun.io/docs/reference/video> for details of what is and isn't supported.

    Examples
    --------
    ### Video with automatically determined frames:
    ```python
    # TODO(#7298): ⚠️ Video is currently only supported in the Rerun web viewer.

    import sys

    import rerun as rr

    if len(sys.argv) < 2:
        # TODO(#7354): Only mp4 is supported for now.
        print(f"Usage: {sys.argv[0]} <path_to_video.[mp4]>")
        sys.exit(1)

    rr.init("rerun_example_asset_video_auto_frames", spawn=True)

    # Log video asset which is referred to by frame references.
    video_asset = rr.AssetVideo(path=sys.argv[1])
    rr.log("video", video_asset, static=True)

    # Send automatically determined video frame timestamps.
    frame_timestamps_ns = video_asset.read_frame_timestamps_ns()
    rr.send_columns(
        "video",
        # Note timeline values don't have to be the same as the video timestamps.
        times=[rr.TimeNanosColumn("video_time", frame_timestamps_ns)],
        components=[rr.VideoFrameReference.indicator(), rr.components.VideoTimestamp.nanoseconds(frame_timestamps_ns)],
    )
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/1200w.png">
      <img src="https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/full.png" width="640">
    </picture>
    </center>

    ### Demonstrates manual use of video frame references:
    ```python
    # TODO(#7298): ⚠️ Video is currently only supported in the Rerun web viewer.

    import sys

    import rerun as rr
    import rerun.blueprint as rrb

    if len(sys.argv) < 2:
        # TODO(#7354): Only mp4 is supported for now.
        print(f"Usage: {sys.argv[0]} <path_to_video.[mp4]>")
        sys.exit(1)

    rr.init("rerun_example_asset_video_manual_frames", spawn=True)

    # Log video asset which is referred to by frame references.
    rr.log("video_asset", rr.AssetVideo(path=sys.argv[1]), static=True)

    # Create two entities, showing the same video frozen at different times.
    rr.log(
        "frame_1s",
        rr.VideoFrameReference(seconds=1.0, video_reference="video_asset"),
    )
    rr.log(
        "frame_2s",
        rr.VideoFrameReference(seconds=2.0, video_reference="video_asset"),
    )

    # Send blueprint that shows two 2D views next to each other.
    rr.send_blueprint(rrb.Horizontal(rrb.Spatial2DView(origin="frame_1s"), rrb.Spatial2DView(origin="frame_2s")))
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/1200w.png">
      <img src="https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/full.png" width="640">
    </picture>
    </center>

    """

    # __init__ can be found in video_frame_reference_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            timestamp=None,
            video_reference=None,
        )

    @classmethod
    def _clear(cls) -> VideoFrameReference:
        """Produce an empty VideoFrameReference, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    @classmethod
    def update_fields(
        cls,
        *,
        clear: bool = False,
        timestamp: datatypes.VideoTimestampLike | None = None,
        video_reference: datatypes.EntityPathLike | None = None,
    ) -> VideoFrameReference:
        """
        Update only some specific fields of a `VideoFrameReference`.

        Parameters
        ----------
        clear:
            If true, all unspecified fields will be explicitly cleared.
        timestamp:
            References the closest video frame to this timestamp.

            Note that this uses the closest video frame instead of the latest at this timestamp
            in order to be more forgiving of rounding errors for inprecise timestamp types.

            Timestamps are relative to the start of the video, i.e. a timestamp of 0 always corresponds to the first frame.
            This is oftentimes equivalent to presentation timestamps (known as PTS), but in the presence of B-frames
            (bidirectionally predicted frames) there may be an offset on the first presentation timestamp in the video.
        video_reference:
            Optional reference to an entity with a [`archetypes.AssetVideo`][rerun.archetypes.AssetVideo].

            If none is specified, the video is assumed to be at the same entity.
            Note that blueprint overrides on the referenced video will be ignored regardless,
            as this is always interpreted as a reference to the data store.

            For a series of video frame references, it is recommended to specify this path only once
            at the beginning of the series and then rely on latest-at query semantics to
            keep the video reference active.

        """

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            kwargs = {
                "timestamp": timestamp,
                "video_reference": video_reference,
            }

            if clear:
                kwargs = {k: v if v is not None else [] for k, v in kwargs.items()}  # type: ignore[misc]

            inst.__attrs_init__(**kwargs)
            return inst

        inst.__attrs_clear__()
        return inst

    @classmethod
    def clear_fields(cls) -> VideoFrameReference:
        """Clear all the fields of a `VideoFrameReference`."""
        inst = cls.__new__(cls)
        inst.__attrs_init__(
            timestamp=[],
            video_reference=[],
        )
        return inst

    timestamp: components.VideoTimestampBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.VideoTimestampBatch._converter,  # type: ignore[misc]
    )
    # References the closest video frame to this timestamp.
    #
    # Note that this uses the closest video frame instead of the latest at this timestamp
    # in order to be more forgiving of rounding errors for inprecise timestamp types.
    #
    # Timestamps are relative to the start of the video, i.e. a timestamp of 0 always corresponds to the first frame.
    # This is oftentimes equivalent to presentation timestamps (known as PTS), but in the presence of B-frames
    # (bidirectionally predicted frames) there may be an offset on the first presentation timestamp in the video.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    video_reference: components.EntityPathBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.EntityPathBatch._converter,  # type: ignore[misc]
    )
    # Optional reference to an entity with a [`archetypes.AssetVideo`][rerun.archetypes.AssetVideo].
    #
    # If none is specified, the video is assumed to be at the same entity.
    # Note that blueprint overrides on the referenced video will be ignored regardless,
    # as this is always interpreted as a reference to the data store.
    #
    # For a series of video frame references, it is recommended to specify this path only once
    # at the beginning of the series and then rely on latest-at query semantics to
    # keep the video reference active.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
