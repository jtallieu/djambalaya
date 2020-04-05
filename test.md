
# Account() Model

<dl class="">
<dt>Does Not Exis</dt>
<dd>adfdf</dd>

<dt>Does Not Exis</dt>
<dd>adfdf</dd>
</dl>

### Properties


#### Class Methods

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |


#### Datas

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| DoesNotExist | Account | data |  |
| MultipleObjectsReturned | Account | data |  |
| __doc__ | Account | data |  |
| __module__ | Account | data |  |
| _default_manager | Account | data |  |
| _meta | Account | data |  |
| _zones | Account | data |  |
| all_devices | Account | data |  |
| all_users | Account | data |  |
| children | Account | data |  |
| Meta | DynamicBaseDnModel | data |  |
| __metaclass__ | Model | data |  |
| _deferred | Model | data |  |
| __dict__ | StateChangeMixin | data |  |
| __weakref__ | StateChangeMixin | data |  |
| __class__ | object | data |  |
| __new__ | object | data |  |


#### Fields

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| access_restriction | ModelBase | field | Array of strings containing access restrictions |
| active_alert_mode | ModelBase | field |  |
| alert_mode | ModelBase | field | Array of strings containing possible alert modes as defined for this account. Accepts an array of any number of strings of varying length. This controls what values are able to be chosen for the &#39;active_alert_mode&#39; field |
| allowable_ip_address_range | ModelBase | field | Limits logins to the address ranges specified |
| billingPlan | ModelBase | field |  |
| brand_subdomain | ModelBase | field |  |
| bridge_sw_group | ModelBase | field |  |
| contact_city | ModelBase | field |  |
| contact_country | ModelBase | field |  |
| contact_email | ModelBase | field |  |
| contact_first_name | ModelBase | field |  |
| contact_last_name | ModelBase | field |  |
| contact_mobile_phone | ModelBase | field |  |
| contact_phone | ModelBase | field |  |
| contact_postal_code | ModelBase | field |  |
| contact_street | ModelBase | field |  |
| contact_utc_offset | ModelBase | field |  |
| custom_domain | ModelBase | field |  |
| default_cluster | ModelBase | field |  |
| feature_flags | ModelBase | field |  |
| id | ModelBase | field |  |
| name | ModelBase | field |  |
| parent_account | ModelBase | field |  |
| pv_params | ModelBase | field | List of perms associated with account |
| session_duration | ModelBase | field |  |
| status | ModelBase | field |  |
| sureview_location_ip | ModelBase | field |  |
| sureview_location_port | ModelBase | field |  |
| timezone | ModelBase | field |  |
| validFrom | ModelBase | field |  |
| web_certificate | ModelBase | field |  |
| web_key | ModelBase | field |  |
| work_days | ModelBase | field | String representation of binary day of the week active |
| work_hours | ModelBase | field | Two entries. Each entry containing a time expressed in local time. The first entry in the array is the work day start time. The second entry in the array is the stop time. Times are represented using a 24 hour clock and are formatted as HHMM |


#### Methods

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| __getattribute__ | Account | method |  |
| __init__ | Account | method |  |
| __str__ | Account | method |  |
| _base_manager | Account | method |  |
| _load_custom_assets | Account | method |  |
| _save_custom_assets | Account | method |  |
| add_account | Account | method |  |
| add_user | Account | method |  |
| clear_shared_camera | Account | method |  |
| feature_flags_to_dict | Account | method |  |
| get_bridge_sw_group_display | Account | method |  |
| get_layout | Account | method |  |
| get_layouts | Account | method |  |
| is_activate_allowed | Account | method |  |
| is_deactivate_allowed | Account | method |  |
| is_delete_allowed | Account | method |  |
| is_edit_allowed | Account | method |  |
| is_pending_allowed | Account | method |  |
| is_status_update_valid | Account | method |  |
| is_suspend_allowed | Account | method |  |
| objects | Account | method |  |
| save | Account | method |  |
| save_static_file | Account | method |  |
| share_camera | Account | method |  |
| __setattr__ | DynamicBaseDnModel | method |  |
| __eq__ | Model | method |  |
| __hash__ | Model | method |  |
| __ne__ | Model | method |  |
| __repr__ | Model | method |  |
| _get_FIELD_display | Model | method |  |
| _get_next_or_previous_by_FIELD | Model | method |  |
| _get_next_or_previous_in_order | Model | method |  |
| _get_pk_val | Model | method |  |
| _get_unique_checks | Model | method |  |
| _perform_date_checks | Model | method |  |
| _perform_unique_checks | Model | method |  |
| _set_pk_val | Model | method |  |
| clean | Model | method |  |
| clean_fields | Model | method |  |
| date_error_message | Model | method |  |
| delete | Model | method |  |
| full_clean | Model | method |  |
| prepare_database_save | Model | method |  |
| save_base | Model | method |  |
| serializable_value | Model | method |  |
| unique_error_message | Model | method |  |
| validate_unique | Model | method |  |
| __reduce__ | StateChangeMixin | method |  |
| current_state | StateChangeMixin | method |  |
| __delattr__ | object | method |  |
| __format__ | object | method |  |
| __reduce_ex__ | object | method |  |
| __sizeof__ | object | method |  |
| __subclasshook__ | object | method |  |


#### Propertys

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| _custom_assets | Account | property |  |
| account_device | Account | property |  |
| active_brand_subdomain | Account | property |  |
| active_white_label_domain | Account | property |  |
| billing_cycle | Account | property |  |
| billing_date | Account | property |  |
| brand_alert_email_url | Account | property |  |
| brand_corp_url | Account | property |  |
| brand_logo_large | Account | property |  |
| brand_logo_small | Account | property |  |
| brand_name | Account | property |  |
| brand_saml_login_url | Account | property |  |
| brand_saml_logout_url | Account | property |  |
| brand_saml_nameid_path | Account | property |  |
| brand_saml_publickey_cert | Account | property |  |
| brand_support_email | Account | property |  |
| brand_support_phone | Account | property |  |
| bridge_sw_versions | Account | property |  |
| bridges | Account | property |  |
| cameras | Account | property |  |
| cameras_owned | Account | property |  |
| customer_id | Account | property |  |
| default_camera_cloud_retention_days | Account | property |  |
| default_camera_full_video_resolution | Account | property |  |
| default_camera_passwords | Account | property |  |
| default_camera_preview_resolution | Account | property |  |
| default_maximum_on_premise_retention_days | Account | property |  |
| default_minimum_on_premise_retention | Account | property |  |
| default_minimum_on_premise_retention_days | Account | property |  |
| enabled_feature_flags | Account | property |  |
| first_responders | Account | property |  |
| gorush_url | Account | property |  |
| inactive_session_timeout | Account | property |  |
| is_active | Account | property |  |
| is_add_delete_disabled | Account | property |  |
| is_advanced_disabled | Account | property |  |
| is_billing_disabled | Account | property |  |
| is_contract_recording | Account | property |  |
| is_custom_brand | Account | property |  |
| is_custom_brand_allowed | Account | property |  |
| is_custom_tos | Account | property |  |
| is_disable_all_settings | Account | property |  |
| is_idp_management | Account | property |  |
| is_inactive | Account | property |  |
| is_master | Account | property |  |
| is_master_allowed | Account | property |  |
| is_master_video_disabled | Account | property |  |
| is_master_video_disabled_allowed | Account | property |  |
| is_mobile_brand | Account | property |  |
| is_mobile_branded | Account | property |  |
| is_motion_image_tagging | Account | property |  |
| is_password_management_enabled | Account | property |  |
| is_pending | Account | property |  |
| is_plugins | Account | property |  |
| is_realm_root | Account | property |  |
| is_rtsp_cameras_enabled | Account | property |  |
| is_standard | Account | property |  |
| is_standard_allowed | Account | property |  |
| is_sub | Account | property |  |
| is_sub_allowed | Account | property |  |
| is_sureview_enabled | Account | property |  |
| is_suspended | Account | property |  |
| is_system_notification_images_enabled | Account | property |  |
| is_system_notifications_disabled | Account | property |  |
| is_tos_disabled | Account | property |  |
| is_two_factor_authentication_forced | Account | property |  |
| is_white_label_domain_enabled | Account | property |  |
| is_white_label_email_enabled | Account | property |  |
| login_attempt_limit | Account | property |  |
| map_lines | Account | property |  |
| notices | Account | property |  |
| owner_account_id | Account | property |  |
| product_edition | Account | property |  |
| pytz | Account | property |  |
| responder_active | Account | property |  |
| saved_filters | Account | property |  |
| users | Account | property |  |
| utc_offset | Account | property |  |
| idp_settings | BrandMixin | property |  |
| is_branded | BrandMixin | property |  |
| pk | Model | property |  |
| password_management_rules | PasswordMixin | property |  |
| password_management_rules_last_change | PasswordMixin | property |  |
| sub_accounts | RelationMixin | property |  |
| is_distributor | StatusMixin | property |  |


#### Static Methods

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |



### Depricated Members


#### Class Methods

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |


#### Datas

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| DoesNotExist | Account | data |  |
| MultipleObjectsReturned | Account | data |  |
| __doc__ | Account | data |  |
| __module__ | Account | data |  |
| _default_manager | Account | data |  |
| _meta | Account | data |  |
| _zones | Account | data |  |
| all_devices | Account | data |  |
| all_users | Account | data |  |
| children | Account | data |  |
| Meta | DynamicBaseDnModel | data |  |
| __metaclass__ | Model | data |  |
| _deferred | Model | data |  |
| __dict__ | StateChangeMixin | data |  |
| __weakref__ | StateChangeMixin | data |  |
| __class__ | object | data |  |
| __new__ | object | data |  |


#### Fields

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| access_restriction | ModelBase | field | Array of strings containing access restrictions |
| active_alert_mode | ModelBase | field |  |
| alert_mode | ModelBase | field | Array of strings containing possible alert modes as defined for this account. Accepts an array of any number of strings of varying length. This controls what values are able to be chosen for the &#39;active_alert_mode&#39; field |
| allowable_ip_address_range | ModelBase | field | Limits logins to the address ranges specified |
| billingPlan | ModelBase | field |  |
| brand_subdomain | ModelBase | field |  |
| bridge_sw_group | ModelBase | field |  |
| contact_city | ModelBase | field |  |
| contact_country | ModelBase | field |  |
| contact_email | ModelBase | field |  |
| contact_first_name | ModelBase | field |  |
| contact_last_name | ModelBase | field |  |
| contact_mobile_phone | ModelBase | field |  |
| contact_phone | ModelBase | field |  |
| contact_postal_code | ModelBase | field |  |
| contact_street | ModelBase | field |  |
| contact_utc_offset | ModelBase | field |  |
| custom_domain | ModelBase | field |  |
| default_cluster | ModelBase | field |  |
| feature_flags | ModelBase | field |  |
| id | ModelBase | field |  |
| name | ModelBase | field |  |
| parent_account | ModelBase | field |  |
| pv_params | ModelBase | field | List of perms associated with account |
| session_duration | ModelBase | field |  |
| status | ModelBase | field |  |
| sureview_location_ip | ModelBase | field |  |
| sureview_location_port | ModelBase | field |  |
| timezone | ModelBase | field |  |
| validFrom | ModelBase | field |  |
| web_certificate | ModelBase | field |  |
| web_key | ModelBase | field |  |
| work_days | ModelBase | field | String representation of binary day of the week active |
| work_hours | ModelBase | field | Two entries. Each entry containing a time expressed in local time. The first entry in the array is the work day start time. The second entry in the array is the stop time. Times are represented using a 24 hour clock and are formatted as HHMM |


#### Methods

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| __getattribute__ | Account | method |  |
| __init__ | Account | method |  |
| __str__ | Account | method |  |
| _base_manager | Account | method |  |
| _load_custom_assets | Account | method |  |
| _save_custom_assets | Account | method |  |
| add_account | Account | method |  |
| add_user | Account | method |  |
| clear_shared_camera | Account | method |  |
| feature_flags_to_dict | Account | method |  |
| get_bridge_sw_group_display | Account | method |  |
| get_layout | Account | method |  |
| get_layouts | Account | method |  |
| is_activate_allowed | Account | method |  |
| is_deactivate_allowed | Account | method |  |
| is_delete_allowed | Account | method |  |
| is_edit_allowed | Account | method |  |
| is_pending_allowed | Account | method |  |
| is_status_update_valid | Account | method |  |
| is_suspend_allowed | Account | method |  |
| objects | Account | method |  |
| save | Account | method |  |
| save_static_file | Account | method |  |
| share_camera | Account | method |  |
| __setattr__ | DynamicBaseDnModel | method |  |
| __eq__ | Model | method |  |
| __hash__ | Model | method |  |
| __ne__ | Model | method |  |
| __repr__ | Model | method |  |
| _get_FIELD_display | Model | method |  |
| _get_next_or_previous_by_FIELD | Model | method |  |
| _get_next_or_previous_in_order | Model | method |  |
| _get_pk_val | Model | method |  |
| _get_unique_checks | Model | method |  |
| _perform_date_checks | Model | method |  |
| _perform_unique_checks | Model | method |  |
| _set_pk_val | Model | method |  |
| clean | Model | method |  |
| clean_fields | Model | method |  |
| date_error_message | Model | method |  |
| delete | Model | method |  |
| full_clean | Model | method |  |
| prepare_database_save | Model | method |  |
| save_base | Model | method |  |
| serializable_value | Model | method |  |
| unique_error_message | Model | method |  |
| validate_unique | Model | method |  |
| __reduce__ | StateChangeMixin | method |  |
| current_state | StateChangeMixin | method |  |
| __delattr__ | object | method |  |
| __format__ | object | method |  |
| __reduce_ex__ | object | method |  |
| __sizeof__ | object | method |  |
| __subclasshook__ | object | method |  |


#### Propertys

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |
| _custom_assets | Account | property |  |
| account_device | Account | property |  |
| active_brand_subdomain | Account | property |  |
| active_white_label_domain | Account | property |  |
| billing_cycle | Account | property |  |
| billing_date | Account | property |  |
| brand_alert_email_url | Account | property |  |
| brand_corp_url | Account | property |  |
| brand_logo_large | Account | property |  |
| brand_logo_small | Account | property |  |
| brand_name | Account | property |  |
| brand_saml_login_url | Account | property |  |
| brand_saml_logout_url | Account | property |  |
| brand_saml_nameid_path | Account | property |  |
| brand_saml_publickey_cert | Account | property |  |
| brand_support_email | Account | property |  |
| brand_support_phone | Account | property |  |
| bridge_sw_versions | Account | property |  |
| bridges | Account | property |  |
| cameras | Account | property |  |
| cameras_owned | Account | property |  |
| customer_id | Account | property |  |
| default_camera_cloud_retention_days | Account | property |  |
| default_camera_full_video_resolution | Account | property |  |
| default_camera_passwords | Account | property |  |
| default_camera_preview_resolution | Account | property |  |
| default_maximum_on_premise_retention_days | Account | property |  |
| default_minimum_on_premise_retention | Account | property |  |
| default_minimum_on_premise_retention_days | Account | property |  |
| enabled_feature_flags | Account | property |  |
| first_responders | Account | property |  |
| gorush_url | Account | property |  |
| inactive_session_timeout | Account | property |  |
| is_active | Account | property |  |
| is_add_delete_disabled | Account | property |  |
| is_advanced_disabled | Account | property |  |
| is_billing_disabled | Account | property |  |
| is_contract_recording | Account | property |  |
| is_custom_brand | Account | property |  |
| is_custom_brand_allowed | Account | property |  |
| is_custom_tos | Account | property |  |
| is_disable_all_settings | Account | property |  |
| is_idp_management | Account | property |  |
| is_inactive | Account | property |  |
| is_master | Account | property |  |
| is_master_allowed | Account | property |  |
| is_master_video_disabled | Account | property |  |
| is_master_video_disabled_allowed | Account | property |  |
| is_mobile_brand | Account | property |  |
| is_mobile_branded | Account | property |  |
| is_motion_image_tagging | Account | property |  |
| is_password_management_enabled | Account | property |  |
| is_pending | Account | property |  |
| is_plugins | Account | property |  |
| is_realm_root | Account | property |  |
| is_rtsp_cameras_enabled | Account | property |  |
| is_standard | Account | property |  |
| is_standard_allowed | Account | property |  |
| is_sub | Account | property |  |
| is_sub_allowed | Account | property |  |
| is_sureview_enabled | Account | property |  |
| is_suspended | Account | property |  |
| is_system_notification_images_enabled | Account | property |  |
| is_system_notifications_disabled | Account | property |  |
| is_tos_disabled | Account | property |  |
| is_two_factor_authentication_forced | Account | property |  |
| is_white_label_domain_enabled | Account | property |  |
| is_white_label_email_enabled | Account | property |  |
| login_attempt_limit | Account | property |  |
| map_lines | Account | property |  |
| notices | Account | property |  |
| owner_account_id | Account | property |  |
| product_edition | Account | property |  |
| pytz | Account | property |  |
| responder_active | Account | property |  |
| saved_filters | Account | property |  |
| users | Account | property |  |
| utc_offset | Account | property |  |
| idp_settings | BrandMixin | property |  |
| is_branded | BrandMixin | property |  |
| pk | Model | property |  |
| password_management_rules | PasswordMixin | property |  |
| password_management_rules_last_change | PasswordMixin | property |  |
| sub_accounts | RelationMixin | property |  |
| is_distributor | StatusMixin | property |  |


#### Static Methods

| Name  | Definition | Document | Dev Note |
| ----: | :--------- | -------- | -------- |



