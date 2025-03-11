# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/video_frame_reference.fbs".

# You can extend this class by creating a "VideoFrameReferenceExt" class in "video_frame_reference_ext.py".

from __future__ import annotations

import numpy as np
import pyarrow as pa
from attrs import define, field

from .. import components, datatypes
from .._baseclasses import (
    Archetype,
    ComponentColumnList,
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
        indexes=[rr.IndexColumn("video_time", timedelta=1e-9 * frame_timestamps_ns)],
        columns=rr.VideoFrameReference.columns_nanoseconds(frame_timestamps_ns),
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
    def from_fields(
        cls,
        *,
        clear_unset: bool = False,
        timestamp: datatypes.VideoTimestampLike | None = None,
        video_reference: datatypes.EntityPathLike | None = None,
    ) -> VideoFrameReference:
        """
        Update only some specific fields of a `VideoFrameReference`.

        Parameters
        ----------
        clear_unset:
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

            if clear_unset:
                kwargs = {k: v if v is not None else [] for k, v in kwargs.items()}  # type: ignore[misc]

            inst.__attrs_init__(**kwargs)
            return inst

        inst.__attrs_clear__()
        return inst

    @classmethod
    def cleared(cls) -> VideoFrameReference:
        """Clear all the fields of a `VideoFrameReference`."""
        return cls.from_fields(clear_unset=True)

    @classmethod
    def columns(
        cls,
        *,
        timestamp: datatypes.VideoTimestampArrayLike | None = None,
        video_reference: datatypes.EntityPathArrayLike | None = None,
    ) -> ComponentColumnList:
        """
        Construct a new column-oriented component bundle.

        This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.

        The returned columns will be partitioned into unit-length sub-batches by default.
        Use `ComponentColumnList.partition` to repartition the data as needed.

        Parameters
        ----------
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
            inst.__attrs_init__(
                timestamp=timestamp,
                video_reference=video_reference,
            )

        batches = inst.as_component_batches(include_indicators=False)
        if len(batches) == 0:
            return ComponentColumnList([])

        kwargs = {"timestamp": timestamp, "video_reference": video_reference}
        columns = []

        for batch in batches:
            arrow_array = batch.as_arrow_array()

            # For primitive arrays and fixed size list arrays, we infer partition size from the input shape.
            if pa.types.is_primitive(arrow_array.type) or pa.types.is_fixed_size_list(arrow_array.type):
                param = kwargs[batch.component_descriptor().archetype_field_name]  # type: ignore[index]
                shape = np.shape(param)  # type: ignore[arg-type]

                batch_length = shape[1] if len(shape) > 1 else 1  # type: ignore[redundant-expr,misc]
                num_rows = shape[0] if len(shape) >= 1 else 1  # type: ignore[redundant-expr,misc]
                sizes = batch_length * np.ones(num_rows)
            else:
                # For non-primitive types, default to partitioning each element separately.
                sizes = np.ones(len(arrow_array))

            columns.append(batch.partition(sizes))

        indicator_column = cls.indicator().partition(np.zeros(len(sizes)))
        return ComponentColumnList([indicator_column] + columns)

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
