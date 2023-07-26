
# Pcap

## Structure

`Pcap`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket` | `string` | Optional | - |
| `max_pkt_len` | `int` | Optional | max_len of non-management packets to capture<br>**Default**: `128`<br>**Constraints**: `<= 128` |

## Example (as JSON)

```json
{
  "bucket": "myorg-pcap",
  "max_pkt_len": 128
}
```

