from enum import Enum


class ExternalResourceV1ResponseBodyResourceType(str, Enum):
    PAGER_DUTY_INCIDENT = "pager_duty_incident"
    OPSGENIE_ALERT = "opsgenie_alert"
    DATADOG_MONITOR_ALERT = "datadog_monitor_alert"
    GITHUB_PULL_REQUEST = "github_pull_request"
    SENTRY_ISSUE = "sentry_issue"
    ATLASSIAN_STATUSPAGE_INCIDENT = "atlassian_statuspage_incident"
    ZENDESK_TICKET = "zendesk_ticket"
    GOOGLE_CALENDAR_EVENT = "google_calendar_event"
    SCRUBBED = "scrubbed"
    STATUSPAGE_INCIDENT = "statuspage_incident"

    def __str__(self) -> str:
        return str(self.value)
