from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserReferencePayloadRequestBody")


@attr.s(auto_attribs=True)
class UserReferencePayloadRequestBody:
    """
    Example:
        {'email': 'Mollitia fugit consequatur.', 'id': 'Et excepturi enim culpa ut.', 'slack_user_id': 'Eos et et
            possimus molestiae rem quia.'}

    Attributes:
        email (Union[Unset, str]): The user's email address, matching the email on their Slack account Example: Magnam
            earum dolorem dicta inventore qui vitae..
        id (Union[Unset, str]): The incident.io ID of a user Example: Harum ut quos repudiandae nesciunt..
        slack_user_id (Union[Unset, str]): The ID of the user's Slack account. Example: Accusantium iure quisquam id..
    """

    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    slack_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        id = self.id
        slack_user_id = self.slack_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        slack_user_id = d.pop("slack_user_id", UNSET)

        user_reference_payload_request_body = cls(
            email=email,
            id=id,
            slack_user_id=slack_user_id,
        )

        user_reference_payload_request_body.additional_properties = d
        return user_reference_payload_request_body

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