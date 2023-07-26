
# Junos Bgp Config

## Structure

`JunosBgpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_key` | `string` | Optional | - |
| `bfd_minimum_interval` | `int` | Optional | default:<br><br>* 1000 if `type`==`external``<br>* 350  `type`==`internal`<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 255000` |
| `communities` | [`List of Community`](../../doc/models/community.md) | Optional | - |
| `disable_bfd` | `bool` | Optional | BFD provides faster path failure detection and is enabled by default<br>**Default**: `False` |
| `export` | `string` | Optional | - |
| `export_policy` | `string` | Optional | default export policies if no per-neighbor policies defined |
| `graceful_restart_time` | `int` | Optional | `0` means disable<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 4095` |
| `hold_time` | `int` | Optional | **Default**: `90`<br>**Constraints**: `>= 0`, `<= 65535` |
| `mimport` | `string` | Optional | - |
| `import_policy` | `string` | Optional | default import policies if no per-neighbor policies defined |
| `imported_networks` | `List of string` | Optional | if policies definition requires this network to exist, this "attaches" the networks to the gateway<br>List of networks that will be learned from this BGP peer |
| `local_as` | `int` | Optional | - |
| `neighbor_as` | `int` | Optional | - |
| `neighbors` | [`dict`](../../doc/models/neighbors.md) | Optional | if per-neighbor as is desired. Property key is the neighbor address |
| `networks` | `List of string` | Optional | if `type`!=`external`or `via`==`wan`networks where we expect BGP neighbor to connect to/from |
| `no_readvertise_to_overlay` | `bool` | Optional | by default, we'll re-advertise all learned BGP routers toward overlay<br>**Default**: `False` |
| `mtype` | [`Type17Enum`](../../doc/models/type-17-enum.md) | Optional | **Constraints**: *Minimum Length*: `1` |
| `via` | [`ViaEnum`](../../doc/models/via-enum.md) | Optional | network name<br>**Default**: `'lan'` |
| `vpn_name` | `string` | Optional | - |
| `wan_name` | `string` | Optional | if `via`==`wan` |

## Example (as JSON)

```json
{
  "bfd_minimum_interval": 0,
  "disable_bfd": false,
  "graceful_restart_time": 0,
  "hold_time": 90,
  "no_readvertise_to_overlay": false,
  "via": "lan",
  "auth_key": "auth_key8",
  "communities": [
    {
      "id": "id9",
      "local_preference": 213,
      "vpn_name": "vpn_name9"
    }
  ],
  "export": "export6"
}
```

