
# Org Setting

Org Settings

## Structure

`OrgSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_device_naming` | [`AutoDeviceNaming`](../../doc/models/auto-device-naming.md) | Optional | - |
| `auto_deviceprofile_assignment` | [`AutoDeviceprofileAssignment`](../../doc/models/auto-deviceprofile-assignment.md) | Optional | - |
| `auto_site_assignment` | [`AutoSiteAssignment`](../../doc/models/auto-site-assignment.md) | Optional | - |
| `blacklist_url` | `string` | Optional | - |
| `cacerts` | `List of string` | Optional | list of PEM-encoded ca certs |
| `celona` | [`Celona`](../../doc/models/celona.md) | Optional | - |
| `cloudshark` | [`Cloudshark`](../../doc/models/cloudshark.md) | Optional | - |
| `cradlepoint` | [`Cradlepoint`](../../doc/models/cradlepoint.md) | Optional | - |
| `created_time` | `float` | Optional | - |
| `device_cert` | [`DeviceCert`](../../doc/models/device-cert.md) | Optional | common device cert, optional |
| `device_updown_threshold` | `int` | Optional | enable threshold-based device down delivery via<br><br>1) device-updowns webhooks topic,<br>2) Mist Alert Framework; e.g. send AP/SW/GW down event only if AP/SW/GW Up is not seen within the threshold in minutes; 0 - 240, default is 0 (trigger immediate)<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 30` |
| `disable_pcap` | `bool` | Optional | whether to disallow Mist to analyze pcap files (this is required for marvis pcap)<br>**Default**: `False` |
| `disable_remote_shell` | `bool` | Optional | whether to disable remote shell access for an entire org<br>**Default**: `False` |
| `for_site` | `bool` | Optional | - |
| `gateway_mgmt` | [`GatewayMgmt`](../../doc/models/gateway-mgmt.md) | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `installer` | [`Installer`](../../doc/models/installer.md) | Optional | - |
| `juniper` | [`Juniper`](../../doc/models/juniper.md) | Optional | - |
| `mgmt` | [`Mgmt`](../../doc/models/mgmt.md) | Optional | management-related properties |
| `mist_nac` | [`MistNac1`](../../doc/models/mist-nac-1.md) | Optional | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `mxedge_mgmt` | [`MxedgeMgmt`](../../doc/models/mxedge-mgmt.md) | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `password_policy` | [`PasswordPolicy`](../../doc/models/password-policy.md) | Optional | password policy |
| `pcap` | [`Pcap`](../../doc/models/pcap.md) | Optional | - |
| `pcap_bucket_verified` | `bool` | Optional | - |
| `security` | [`Security`](../../doc/models/security.md) | Optional | - |
| `simple_alert` | [`SimpleAlert`](../../doc/models/simple-alert.md) | Optional | Set of heuristic rules will be enabled when marvis subscription is not available.<br>It triggers when, in a Z minute window, there are more than Y distinct client encountring over X failures |
| `site_id` | `uuid\|string` | Optional | - |
| `switch_mgmt` | [`SwitchMgmt3`](../../doc/models/switch-mgmt-3.md) | Optional | - |
| `synthetic_test` | [`SyntheticTest`](../../doc/models/synthetic-test.md) | Optional | - |
| `tags` | `List of string` | Optional | list of tags |
| `ui_idle_timeout` | `int` | Optional | automatically logout the user when UI session is inactive. `0` means disabled<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 480` |
| `vpn_options` | [`VpnOptions`](../../doc/models/vpn-options.md) | Optional | - |
| `wan_pma` | [`WanPma`](../../doc/models/wan-pma.md) | Optional | - |
| `wired_pma` | [`WiredPma`](../../doc/models/wired-pma.md) | Optional | - |

## Example (as JSON)

```json
{
  "blacklist_url": "https://papi.s3.amazonaws.com/blacklist/xxx...",
  "device_updown_threshold": 0,
  "disable_pcap": false,
  "disable_remote_shell": false,
  "ui_idle_timeout": 10,
  "auto_device_naming": {
    "enable": false,
    "rules": [
      {
        "expression": "expression0",
        "model": "model0",
        "prefix": "prefix0",
        "src": "name",
        "subnet": "subnet0",
        "suffix": "suffix8"
      },
      {
        "expression": "expression9",
        "model": "model9",
        "prefix": "prefix1",
        "src": "lldp_port_desc",
        "subnet": "subnet1",
        "suffix": "suffix7"
      }
    ]
  },
  "auto_deviceprofile_assignment": {
    "enable": false,
    "rules": [
      {
        "expression": "expression6",
        "model": "model4",
        "prefix": "prefix4",
        "src": "model",
        "subnet": "subnet4",
        "suffix": "suffix4"
      }
    ]
  },
  "auto_site_assignment": {
    "enable": false,
    "rules": [
      {
        "expression": "expression6",
        "model": "model4",
        "prefix": "prefix4",
        "src": "model",
        "subnet": "subnet4",
        "suffix": "suffix4"
      }
    ]
  },
  "cacerts": [
    "cacerts0"
  ]
}
```

