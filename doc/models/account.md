
# Account

## Structure

`Account`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Optional | Linked apps(zoom/teams/intune/jamf) tenant id |
| `error` | `string` | Optional | This error is provided only when the apps(zoom) account refresh token fails in the backend |
| `last_status` | `object` | Optional | - |
| `last_sync` | `object` | Optional | - |
| `linked_by` | `string` | Optional | First name of the user who linked the apps(zoom/teams/intune/jamf) account |
| `name` | `string` | Optional | Name of the company whose (zoom/teams/intune/jamf) account mist has subscribed to |

## Example (as JSON)

```json
{
  "account_id": "account_id2",
  "error": "error4",
  "last_status": {
    "key1": "val1",
    "key2": "val2"
  },
  "last_sync": {
    "key1": "val1",
    "key2": "val2"
  },
  "linked_by": "linked_by2"
}
```

