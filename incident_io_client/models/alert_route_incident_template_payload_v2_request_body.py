from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_incident_template_payload_v2_request_body_priority_severity import (
    AlertRouteIncidentTemplatePayloadV2RequestBodyPrioritySeverity,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_incident_template_payload_v2_request_body_custom_field_priorities import (
        AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFieldPriorities,
    )
    from ..models.alert_route_incident_template_payload_v2_request_body_custom_fields import (
        AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFields,
    )
    from ..models.engine_param_binding_payload_v2_request_body import (
        EngineParamBindingPayloadV2RequestBody,
    )


T = TypeVar("T", bound="AlertRouteIncidentTemplatePayloadV2RequestBody")


@_attrs_define
class AlertRouteIncidentTemplatePayloadV2RequestBody:
    """
    Example:
        {'custom_field_priorities': {'abc123': 'abc123'}, 'custom_fields': {'custom_field_10014': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'incident_mode': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_type':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'name': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity':
            'severity-first-wins', 'severity': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'summary': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'workspace': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        custom_field_priorities (AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFieldPriorities): lookup of the
            priority options for each custom field in the template Example: {'abc123': 'abc123'}.
        priority_severity (AlertRouteIncidentTemplatePayloadV2RequestBodyPrioritySeverity): option defining whether to
            cause subsequent alerts to increase the severity Example: severity-first-wins.
        custom_fields (Union[Unset, AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFields]): Custom field keys
            mapped to values Example: {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}.
        incident_mode (Union[Unset, EngineParamBindingPayloadV2RequestBody]):  Example: {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        incident_type (Union[Unset, EngineParamBindingPayloadV2RequestBody]):  Example: {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        name (Union[Unset, EngineParamBindingPayloadV2RequestBody]):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        severity (Union[Unset, EngineParamBindingPayloadV2RequestBody]):  Example: {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        summary (Union[Unset, EngineParamBindingPayloadV2RequestBody]):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        workspace (Union[Unset, EngineParamBindingPayloadV2RequestBody]):  Example: {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    custom_field_priorities: "AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFieldPriorities"
    priority_severity: AlertRouteIncidentTemplatePayloadV2RequestBodyPrioritySeverity
    custom_fields: Union[Unset, "AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFields"] = (
        UNSET
    )
    incident_mode: Union[Unset, "EngineParamBindingPayloadV2RequestBody"] = UNSET
    incident_type: Union[Unset, "EngineParamBindingPayloadV2RequestBody"] = UNSET
    name: Union[Unset, "EngineParamBindingPayloadV2RequestBody"] = UNSET
    severity: Union[Unset, "EngineParamBindingPayloadV2RequestBody"] = UNSET
    summary: Union[Unset, "EngineParamBindingPayloadV2RequestBody"] = UNSET
    workspace: Union[Unset, "EngineParamBindingPayloadV2RequestBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_priorities = self.custom_field_priorities.to_dict()

        priority_severity = self.priority_severity.value

        custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        incident_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incident_mode, Unset):
            incident_mode = self.incident_mode.to_dict()

        incident_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incident_type, Unset):
            incident_type = self.incident_type.to_dict()

        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        workspace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_priorities": custom_field_priorities,
                "priority_severity": priority_severity,
            }
        )
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if incident_mode is not UNSET:
            field_dict["incident_mode"] = incident_mode
        if incident_type is not UNSET:
            field_dict["incident_type"] = incident_type
        if name is not UNSET:
            field_dict["name"] = name
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_route_incident_template_payload_v2_request_body_custom_field_priorities import (
            AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFieldPriorities,
        )
        from ..models.alert_route_incident_template_payload_v2_request_body_custom_fields import (
            AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFields,
        )
        from ..models.engine_param_binding_payload_v2_request_body import (
            EngineParamBindingPayloadV2RequestBody,
        )

        d = src_dict.copy()
        custom_field_priorities = (
            AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFieldPriorities.from_dict(
                d.pop("custom_field_priorities")
            )
        )

        priority_severity = AlertRouteIncidentTemplatePayloadV2RequestBodyPrioritySeverity(
            d.pop("priority_severity")
        )

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = AlertRouteIncidentTemplatePayloadV2RequestBodyCustomFields.from_dict(
                _custom_fields
            )

        _incident_mode = d.pop("incident_mode", UNSET)
        incident_mode: Union[Unset, EngineParamBindingPayloadV2RequestBody]
        if isinstance(_incident_mode, Unset):
            incident_mode = UNSET
        else:
            incident_mode = EngineParamBindingPayloadV2RequestBody.from_dict(_incident_mode)

        _incident_type = d.pop("incident_type", UNSET)
        incident_type: Union[Unset, EngineParamBindingPayloadV2RequestBody]
        if isinstance(_incident_type, Unset):
            incident_type = UNSET
        else:
            incident_type = EngineParamBindingPayloadV2RequestBody.from_dict(_incident_type)

        _name = d.pop("name", UNSET)
        name: Union[Unset, EngineParamBindingPayloadV2RequestBody]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = EngineParamBindingPayloadV2RequestBody.from_dict(_name)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, EngineParamBindingPayloadV2RequestBody]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = EngineParamBindingPayloadV2RequestBody.from_dict(_severity)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, EngineParamBindingPayloadV2RequestBody]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = EngineParamBindingPayloadV2RequestBody.from_dict(_summary)

        _workspace = d.pop("workspace", UNSET)
        workspace: Union[Unset, EngineParamBindingPayloadV2RequestBody]
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = EngineParamBindingPayloadV2RequestBody.from_dict(_workspace)

        alert_route_incident_template_payload_v2_request_body = cls(
            custom_field_priorities=custom_field_priorities,
            priority_severity=priority_severity,
            custom_fields=custom_fields,
            incident_mode=incident_mode,
            incident_type=incident_type,
            name=name,
            severity=severity,
            summary=summary,
            workspace=workspace,
        )

        alert_route_incident_template_payload_v2_request_body.additional_properties = d
        return alert_route_incident_template_payload_v2_request_body

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
