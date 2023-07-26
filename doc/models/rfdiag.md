
# Rfdiag

RF Diag

## Structure

`Rfdiag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duration` | `int` | Optional | recording length in seconds, max is 180. Default value is also 180.<br>**Default**: `180`<br>**Constraints**: `<= 180` |
| `mac` | `string` | Optional | if `type`==`client` or `asset`, mac of the device |
| `name` | `string` | Required | name of the recording, the name of the sdk client would be a good default choice |
| `sdkclient_id` | `uuid\|string` | Optional | if `type`==`sdkclient`, sdkclient_id of this recording |
| `mtype` | [`Type36Enum`](../../doc/models/type-36-enum.md) | Required | sdkclient / client/ asset |

## Example (as JSON)

```json
{
  "duration": 180,
  "name": "name0",
  "type": "asset",
  "mac": "mac4",
  "sdkclient_id": "000011ec-0000-0000-0000-000000000000"
}
```

