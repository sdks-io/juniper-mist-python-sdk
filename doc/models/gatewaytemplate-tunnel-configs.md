
# Gatewaytemplate Tunnel Configs

## Structure

`GatewaytemplateTunnelConfigs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_provision` | [`AutoProvision`](../../doc/models/auto-provision.md) | Optional | - |
| `ike_lifetime` | `int` | Optional | Only if:<br><br>* `provider`== `custom-ipsec` |
| `ike_mode` | [`IkeModeEnum`](../../doc/models/ike-mode-enum.md) | Optional | Only if:<br><br>* `provider`== `custom-ipsec`<br>**Default**: `'main'` |
| `ike_proposals` | [`List of IkeProposal`](../../doc/models/ike-proposal.md) | Optional | if `provider`== `custom-ipsec` |
| `ipsec_lifetime` | `int` | Optional | if `provider`== `custom-ipsec` |
| `ipsec_proposals` | [`List of IpsecProposal`](../../doc/models/ipsec-proposal.md) | Optional | Only if:<br><br>* `provider`== `custom-ipsec` |
| `local_id` | `string` | Optional | Only if:<br><br>* `provider`== `zscaler-ipsec`<br>* `provider`==`jse-ipsec`<br>* `provider`== `custom-ipsec` |
| `mode` | [`ModeEnum`](../../doc/models/mode-enum.md) | Optional | **Default**: `'active-standby'` |
| `primary` | [`Primary1`](../../doc/models/primary-1.md) | Optional | - |
| `probe` | [`Probe`](../../doc/models/probe.md) | Optional | Only if:<br><br>* `provider`== `custom-ipsec` |
| `protocol` | [`Protocol1Enum`](../../doc/models/protocol-1-enum.md) | Optional | Only if:<br><br>* `provider`== `custom-ipsec` |
| `provider` | [`ProviderEnum`](../../doc/models/provider-enum.md) | Optional | - |
| `psk` | `string` | Optional | Only if:<br><br>* `provider`== `zscaler-ipsec`<br>* `provider`==`jse-ipsec`<br>* `provider`== `custom-ipsec` |
| `secondary` | [`Secondary1`](../../doc/models/secondary-1.md) | Optional | - |
| `version` | [`VersionEnum`](../../doc/models/version-enum.md) | Optional | Only if:<br><br>* `provider`== `custom-gre`<br>* `provider`== `custom-ipsec`<br>**Default**: `'2'` |

## Example (as JSON)

```json
{
  "ike_mode": "main",
  "mode": "active-standby",
  "version": "2",
  "auto_provision": {
    "enable": false,
    "latlng": {
      "lat": 97.24,
      "lng": 70.22
    },
    "primary": {
      "num_hosts": "num_hosts6",
      "wan_names": [
        "wan_names8",
        "wan_names9"
      ]
    },
    "region": "auto",
    "secondary": {
      "num_hosts": "num_hosts8",
      "wan_names": [
        "wan_names0",
        "wan_names1"
      ]
    }
  },
  "ike_lifetime": 42,
  "ike_proposals": [
    {
      "auth_algo": "sha2",
      "dh_group": "21",
      "enc_algo": "aes_gcm256"
    }
  ],
  "ipsec_lifetime": 102
}
```

