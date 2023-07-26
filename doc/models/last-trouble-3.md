
# Last Trouble 3

last trouble code of switch

## Structure

`LastTrouble3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | Codes:<br><br>- 102   No DHCP lease received on any interface<br>- 103   No default gateway<br>- 104   Gateway unreachable<br>- 105   No DNS server<br>- 106   DNS lookup failed<br>- 108   Agent cannot connect to controller<br>- 109   Authentication failed<br>- 110   Underlying service (i.e. Netconf/SSH/HTTPS) is down<br>- 113   DNS failure with Mist cloud<br>- 114   Empty DNS response with Mist cloud |
| `timestamp` | `int` | Required | - |

## Example (as JSON)

```json
{
  "code": "code8",
  "timestamp": 82
}
```

