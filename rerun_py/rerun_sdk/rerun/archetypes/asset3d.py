# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/asset3d.fbs".

# You can extend this class by creating a "Asset3DExt" class in "asset3d_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components, datatypes
from .._baseclasses import (
    Archetype,
)
from ..error_utils import catch_and_log_exceptions
from .asset3d_ext import Asset3DExt

__all__ = ["Asset3D"]


@define(str=False, repr=False, init=False)
class Asset3D(Asset3DExt, Archetype):
    """
    **Archetype**: A prepacked 3D asset (`.gltf`, `.glb`, `.obj`, `.stl`, etc.).

    See also [`archetypes.Mesh3D`][rerun.archetypes.Mesh3D].

    If there are multiple [`archetypes.InstancePoses3D`][rerun.archetypes.InstancePoses3D] instances logged to the same entity as a mesh,
    an instance of the mesh will be drawn for each transform.

    Example
    -------
    ### Simple 3D asset:
    ```python
    import sys

    import rerun as rr

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_asset.[gltf|glb|obj|stl]>")
        sys.exit(1)

    rr.init("rerun_example_asset3d", spawn=True)

    rr.log("world", rr.ViewCoordinates.RIGHT_HAND_Z_UP, static=True)  # Set an up-axis
    rr.log("world/asset", rr.Asset3D(path=sys.argv[1]))
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/asset3d_simple/af238578188d3fd0de3e330212120e2842a8ddb2/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/asset3d_simple/af238578188d3fd0de3e330212120e2842a8ddb2/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/asset3d_simple/af238578188d3fd0de3e330212120e2842a8ddb2/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/asset3d_simple/af238578188d3fd0de3e330212120e2842a8ddb2/1200w.png">
      <img src="https://static.rerun.io/asset3d_simple/af238578188d3fd0de3e330212120e2842a8ddb2/full.png" width="640">
    </picture>
    </center>

    """

    # __init__ can be found in asset3d_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            blob=None,
            media_type=None,
            albedo_factor=None,
        )

    @classmethod
    def _clear(cls) -> Asset3D:
        """Produce an empty Asset3D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    @classmethod
    def update_fields(
        cls,
        *,
        clear: bool = False,
        blob: datatypes.BlobLike | None = None,
        media_type: datatypes.Utf8Like | None = None,
        albedo_factor: datatypes.Rgba32Like | None = None,
    ) -> Asset3D:
        """
        Update only some specific fields of a `Asset3D`.

        Parameters
        ----------
        clear:
            If true, all unspecified fields will be explicitly cleared.
        blob:
            The asset's bytes.
        media_type:
            The Media Type of the asset.

            Supported values:
            * `model/gltf-binary`
            * `model/gltf+json`
            * `model/obj` (.mtl material files are not supported yet, references are silently ignored)
            * `model/stl`

            If omitted, the viewer will try to guess from the data blob.
            If it cannot guess, it won't be able to render the asset.
        albedo_factor:
            A color multiplier applied to the whole asset.

            For mesh who already have `albedo_factor` in materials,
            it will be overwritten by actual `albedo_factor` of [`archetypes.Asset3D`][rerun.archetypes.Asset3D] (if specified).

        """

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            kwargs = {
                "blob": blob,
                "media_type": media_type,
                "albedo_factor": albedo_factor,
            }

            if clear:
                kwargs = {k: v if v is not None else [] for k, v in kwargs.items()}  # type: ignore[misc]

            inst.__attrs_init__(**kwargs)
            return inst

        inst.__attrs_clear__()
        return inst

    @classmethod
    def clear_fields(cls) -> Asset3D:
        """Clear all the fields of a `Asset3D`."""
        inst = cls.__new__(cls)
        inst.__attrs_init__(
            blob=[],
            media_type=[],
            albedo_factor=[],
        )
        return inst

    blob: components.BlobBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.BlobBatch._converter,  # type: ignore[misc]
    )
    # The asset's bytes.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    media_type: components.MediaTypeBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.MediaTypeBatch._converter,  # type: ignore[misc]
    )
    # The Media Type of the asset.
    #
    # Supported values:
    # * `model/gltf-binary`
    # * `model/gltf+json`
    # * `model/obj` (.mtl material files are not supported yet, references are silently ignored)
    # * `model/stl`
    #
    # If omitted, the viewer will try to guess from the data blob.
    # If it cannot guess, it won't be able to render the asset.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    albedo_factor: components.AlbedoFactorBatch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AlbedoFactorBatch._converter,  # type: ignore[misc]
    )
    # A color multiplier applied to the whole asset.
    #
    # For mesh who already have `albedo_factor` in materials,
    # it will be overwritten by actual `albedo_factor` of [`archetypes.Asset3D`][rerun.archetypes.Asset3D] (if specified).
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
