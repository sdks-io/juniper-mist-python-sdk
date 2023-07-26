
# Secpolicy

Security Policy is designed to audit / catch discripancies between “what’s intended to be running” versus “what’s actually running” in a network. Many big organizations have separated Security and IT team (for good reasons). Each site can be assigned a security policy. Whenever an AP is provisioned, the configuration will be checked against the security policy. Any violations will be flagged in Device Config History where you can search for the when and where the violation occurs.

## Structure

`Secpolicy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `wlans` | [`List of Wlan`](../../doc/models/wlan.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "name": "name0",
  "org_id": "00000ec8-0000-0000-0000-000000000000"
}
```

