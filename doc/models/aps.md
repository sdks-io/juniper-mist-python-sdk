
# Aps

Property key is the AP MAC address (e.g. "5c5b35000001"). All optionals, parent parameters will be used if not defined

## Structure

`Aps`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band` | [`Band3Enum`](../../doc/models/band-3-enum.md) | Optional | Only Single value allowed<br>**Default**: `'24'` |
| `channel` | `string` | Optional | specify the channel value where scan PCAP has to be started |
| `tcpdump_expression` | `string` | Optional | tcpdump expression, port specific if specified under ports dict, otherwise applicable across ports if specified at top level of payload. Port specific value overrides top level value when both exist. |
| `width` | `string` | Optional | specify the bandwidth value with respect to the channel. |

## Example (as JSON)

```json
{
  "band": "24",
  "channel": "channel4",
  "tcpdump_expression": "tcpdump_expression0",
  "width": "width6"
}
```

