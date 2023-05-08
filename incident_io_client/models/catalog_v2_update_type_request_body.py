from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.catalog_v2_update_type_request_body_color import (
    CatalogV2UpdateTypeRequestBodyColor,
)
from ..models.catalog_v2_update_type_request_body_icon import (
    CatalogV2UpdateTypeRequestBodyIcon,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_v2_update_type_request_body_annotations import (
        CatalogV2UpdateTypeRequestBodyAnnotations,
    )


T = TypeVar("T", bound="CatalogV2UpdateTypeRequestBody")


@attr.s(auto_attribs=True)
class CatalogV2UpdateTypeRequestBody:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'bolt', 'name': 'Kubernetes Cluster',
            'ranked': True, 'semantic_type': 'custom', 'type_name': 'CatalogEntry["01FCNDV6P870EA6S7TK1DSYDG2"]'}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        annotations (Union[Unset, CatalogV2UpdateTypeRequestBodyAnnotations]): Annotations that can track metadata about
            this type Example: {'incident.io/catalog-importer/id': 'id-of-config'}.
        color (Union[Unset, CatalogV2UpdateTypeRequestBodyColor]): Sets the display color of this type in the dashboard
            Example: slate.
        icon (Union[Unset, CatalogV2UpdateTypeRequestBodyIcon]): Sets the display icon of this type in the dashboard
            Example: bolt.
        ranked (Union[Unset, bool]): If this type should be ranked Example: True.
        semantic_type (Union[Unset, str]): Semantic type of this resource Example: custom.
        type_name (Union[Unset, str]): The type name of this catalog type, to be used when defining attributes Example:
            CatalogEntry["01FCNDV6P870EA6S7TK1DSYDG2"].
    """

    description: str
    name: str
    annotations: Union[Unset, "CatalogV2UpdateTypeRequestBodyAnnotations"] = UNSET
    color: Union[Unset, CatalogV2UpdateTypeRequestBodyColor] = UNSET
    icon: Union[Unset, CatalogV2UpdateTypeRequestBodyIcon] = UNSET
    ranked: Union[Unset, bool] = UNSET
    semantic_type: Union[Unset, str] = UNSET
    type_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.value

        ranked = self.ranked
        semantic_type = self.semantic_type
        type_name = self.type_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if semantic_type is not UNSET:
            field_dict["semantic_type"] = semantic_type
        if type_name is not UNSET:
            field_dict["type_name"] = type_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_v2_update_type_request_body_annotations import (
            CatalogV2UpdateTypeRequestBodyAnnotations,
        )

        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, CatalogV2UpdateTypeRequestBodyAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CatalogV2UpdateTypeRequestBodyAnnotations.from_dict(_annotations)

        _color = d.pop("color", UNSET)
        color: Union[Unset, CatalogV2UpdateTypeRequestBodyColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CatalogV2UpdateTypeRequestBodyColor(_color)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, CatalogV2UpdateTypeRequestBodyIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = CatalogV2UpdateTypeRequestBodyIcon(_icon)

        ranked = d.pop("ranked", UNSET)

        semantic_type = d.pop("semantic_type", UNSET)

        type_name = d.pop("type_name", UNSET)

        catalog_v2_update_type_request_body = cls(
            description=description,
            name=name,
            annotations=annotations,
            color=color,
            icon=icon,
            ranked=ranked,
            semantic_type=semantic_type,
            type_name=type_name,
        )

        catalog_v2_update_type_request_body.additional_properties = d
        return catalog_v2_update_type_request_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties