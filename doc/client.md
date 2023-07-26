
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `authorization` | `string` | Auth Header. Replace {x-auth-key} with your Auth Key.<br>*Default*: `'Token {x-auth-key}'` |

The API client can be initialized as follows:

```python
from mistapi.mistapi_client import MistapiClient
from mistapi.configuration import Environment

client = MistapiClient(
    authorization='Token {x-auth-key}'
)
```

## Mist API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| login | Gets LoginController |
| login_with_o_auth_2 | Gets LoginWithOAuth2Controller |
| api_token | Gets APITokenController |
| installer | Gets InstallerController |
| admin | Gets AdminController |
| mobile | Gets MobileController |
| msps | Gets MspsController |
| msps_admins | Gets MspsAdminsController |
| msps_inventory | Gets MspsInventoryController |
| msps_invites | Gets MspsInvitesController |
| msps_logo | Gets MspsLogoController |
| msps_logs | Gets MspsLogsController |
| msps_licenses | Gets MspsLicensesController |
| msps_marvis | Gets MspsMarvisController |
| msps_org_groups | Gets MspsOrgGroupsController |
| msps_orgs | Gets MspsOrgsController |
| msps_sl_es | Gets MspsSLEsController |
| msps_sso_roles | Gets MspsSSORolesController |
| msps_sso | Gets MspsSSOController |
| msps_stats | Gets MspsStatsController |
| msps_tickets | Gets MspsTicketsController |
| orgs_admins | Gets OrgsAdminsController |
| sites | Gets SitesController |
| sites_alarms | Gets SitesAlarmsController |
| sites_applications | Gets SitesApplicationsController |
| sites_anomaly | Gets SitesAnomalyController |
| sites_asset_filters | Gets SitesAssetFiltersController |
| sites_assets | Gets SitesAssetsController |
| sites_beacons | Gets SitesBeaconsController |
| sites_calls | Gets SitesCallsController |
| sites_clients_wan | Gets SitesClientsWanController |
| sites_clients_wired | Gets SitesClientsWiredController |
| sites_clients_wireless | Gets SitesClientsWirelessController |
| sites_devices | Gets SitesDevicesController |
| sites_devices_wireless | Gets SitesDevicesWirelessController |
| sites_devices_others | Gets SitesDevicesOthersController |
| sites_devices_wired | Gets SitesDevicesWiredController |
| sites_devices_wired_virtual_chassis | Gets SitesDevicesWiredVirtualChassisController |
| sites_devices_wan | Gets SitesDevicesWANController |
| sites_devices_wan_ha | Gets SitesDevicesWANHAController |
| sites_devices_stats | Gets SitesDevicesStatsController |
| sites_devices_upgrades | Gets SitesDevicesUpgradesController |
| sites_devices_utilities | Gets SitesDevicesUtilitiesController |
| sites_events | Gets SitesEventsController |
| sites_evpn_topologies | Gets SitesEVPNTopologiesController |
| sites_guests | Gets SitesGuestsController |
| sites_insights | Gets SitesInsightsController |
| sites_licenses | Gets SitesLicensesController |
| sites_location | Gets SitesLocationController |
| sites_maps | Gets SitesMapsController |
| sites_maps_auto_orientation | Gets SitesMapsAutoOrientationController |
| sites_maps_auto_placement | Gets SitesMapsAutoPlacementController |
| sites_mx_edges | Gets SitesMxEdgesController |
| sites_mx_tunnels | Gets SitesMxTunnelsController |
| sites_networks | Gets SitesNetworksController |
| sites_pcaps | Gets SitesPcapsController |
| sites_psks | Gets SitesPsksController |
| sites_rfdiags | Gets SitesRfdiagsController |
| sites_rogues | Gets SitesRoguesController |
| sites_rrm | Gets SitesRRMController |
| sites_rssizones | Gets SitesRssizonesController |
| sites_services | Gets SitesServicesController |
| sites_service_policies | Gets SitesServicePoliciesController |
| sites_setting | Gets SitesSettingController |
| sites_skyatp | Gets SitesSkyatpController |
| sites_sl_es | Gets SitesSLEsController |
| sites_stats | Gets SitesStatsController |
| sites_subscriptions | Gets SitesSubscriptionsController |
| sites_synthetic_tests | Gets SitesSyntheticTestsController |
| sites_ui_settings | Gets SitesUISettingsController |
| sites_v_beacons | Gets SitesVBeaconsController |
| sites_vp_ns | Gets SitesVPNsController |
| sites_webhooks | Gets SitesWebhooksController |
| sites_wlans | Gets SitesWlansController |
| sites_wx_rules | Gets SitesWxRulesController |
| sites_wx_tags | Gets SitesWxTagsController |
| sites_wx_tunnels | Gets SitesWxTunnelsController |
| sites_zones | Gets SitesZonesController |
| constants | Gets ConstantsController |
| self | Gets SelfController |
| webhook_samples | Gets WebhookSamplesController |
| orgs_admin | Gets OrgsAdminController |

