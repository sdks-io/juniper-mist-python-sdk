
# Sessions 2

## Structure

`Sessions2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_as_session_id` | `string` | Optional | if `use_ap_as_session_ids`==`true`, only apmac is supported right now. This is the name WLAN should use for wxtunnel_remote_id |
| `comment` | `string` | Optional | optional, user-specified string for display purpose |
| `enable_cookie` | `bool` | Optional | - |
| `ethertype` | [`EthertypeEnum`](../../doc/models/ethertype-enum.md) | Optional | - |
| `local_session_id` | `int` | Optional | 1-4294967295<br>**Constraints**: `>= 1`, `<= 4294967295` |
| `pseudo_802_1_ad_enabled` | `bool` | Optional | optional. Enables the pseudo 802.1ad QinQ mode where the AP device drops the outer vlan tag (QinQ). This mode is useful when tunneling Mist AP’s to some aggregation routers.<br>**Default**: `False` |
| `remote_id` | `string` | Optional | remote-id of the session, has to be unique in the same tunnel |
| `remote_session_id` | `int` | Optional | 1-4294967295<br>**Constraints**: `>= 1`, `<= 4294967295` |
| `use_ap_as_session_ids` | `bool` | Optional | whether to use AP (last 4 bytes of MAC currently) as session ids<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "pseudo_802-1ad_enabled": false,
  "use_ap_as_session_ids": false,
  "ap_as_session_id": "ap_as_session_id8",
  "comment": "comment6",
  "enable_cookie": false,
  "ethertype": "ethernet",
  "local_session_id": 246
}
```

