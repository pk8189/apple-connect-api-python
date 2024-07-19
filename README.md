
# App Store Connect API Python SDK

## Overview


## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from apple_python import Client
from os import getenv

Client(token=getenv("API_TOKEN"))
```

### Asynchronous Client
```python
from apple_python import AsyncClient
from os import getenv

AsyncClient(token=getenv("API_TOKEN"))
```


### 
> 

```python
client.v1.alternative_distribution_domains.delete(id="string")
```

---

### 
> 

```python
client.v1.alternative_distribution_keys.delete(id="string")
```

---

### 
> 

```python
client.v1.analytics_report_requests.delete(id="string")
```

---

### 
> 

```python
client.v1.app_clip_default_experience_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.delete(id="string")
```

---

### 
> 

```python
client.v1.app_clip_header_images.delete(id="string")
```

---

### 
> 

```python
client.v1.app_custom_product_page_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.app_custom_product_pages.delete(id="string")
```

---

### 
> 

```python
client.v1.app_event_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.app_event_screenshots.delete(id="string")
```

---

### 
> 

```python
client.v1.app_event_video_clips.delete(id="string")
```

---

### 
> 

```python
client.v1.app_events.delete(id="string")
```

---

### 
> 

```python
client.v1.app_info_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.app_pre_orders.delete(id="string")
```

---

### 
> 

```python
client.v1.app_preview_sets.delete(id="string")
```

---

### 
> 

```python
client.v1.app_previews.delete(id="string")
```

---

### 
> 

```python
client.v1.app_screenshot_sets.delete(id="string")
```

---

### 
> 

```python
client.v1.app_screenshots.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_review_attachments.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatment_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatments.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_version_experiments.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_version_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_version_phased_releases.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_version_submissions.delete(id="string")
```

---

### 
> 

```python
client.v1.app_store_versions.delete(id="string")
```

---

### 
> 

```python
client.v1.apps.relationships.beta_testers.delete(
    id="string", data={"data": [{"id": "string", "type": "betaTesters"}]}
)
```

---

### 
> 

```python
client.v1.beta_app_clip_invocation_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.beta_app_clip_invocations.delete(id="string")
```

---

### 
> 

```python
client.v1.beta_app_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.beta_build_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.beta_groups.delete(id="string")
```

---

### 
> 

```python
client.v1.beta_groups.relationships.beta_testers.delete(
    id="string", data={"data": [{"id": "string", "type": "betaTesters"}]}
)
```

---

### 
> 

```python
client.v1.beta_groups.relationships.builds.delete(
    id="string", data={"data": [{"id": "string", "type": "builds"}]}
)
```

---

### 
> 

```python
client.v1.beta_testers.delete(id="string")
```

---

### 
> 

```python
client.v1.beta_testers.relationships.apps.delete(
    id="string", data={"data": [{"id": "string", "type": "apps"}]}
)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.beta_groups.delete(
    id="string", data={"data": [{"id": "string", "type": "betaGroups"}]}
)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.builds.delete(
    id="string", data={"data": [{"id": "string", "type": "builds"}]}
)
```

---

### 
> 

```python
client.v1.builds.relationships.beta_groups.delete(
    id="string", data={"data": [{"id": "string", "type": "betaGroups"}]}
)
```

---

### 
> 

```python
client.v1.builds.relationships.individual_testers.delete(
    id="string", data={"data": [{"id": "string", "type": "betaTesters"}]}
)
```

---

### 
> 

```python
client.v1.bundle_id_capabilities.delete(id="string")
```

---

### 
> 

```python
client.v1.bundle_ids.delete(id="string")
```

---

### 
> 

```python
client.v1.certificates.delete(id="string")
```

---

### 
> 

```python
client.v1.ci_products.delete(id="string")
```

---

### 
> 

```python
client.v1.ci_workflows.delete(id="string")
```

---

### 
> 

```python
client.v1.customer_review_responses.delete(id="string")
```

---

### 
> 

```python
client.v1.end_user_license_agreements.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_achievement_images.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_achievement_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_achievement_releases.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_achievements.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_app_versions.relationships.compatibility_versions.delete(
    id="string", data={"data": [{"id": "string", "type": "gameCenterAppVersions"}]}
)
```

---

### 
> 

```python
client.v1.game_center_enabled_versions.relationships.compatible_versions.delete(
    id="string", data={"data": [{"id": "string", "type": "gameCenterEnabledVersions"}]}
)
```

---

### 
> 

```python
client.v1.game_center_groups.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_images.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_releases.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_images.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_member_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_releases.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.relationships.game_center_leaderboards.delete(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboards"}]}
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rules.delete(id="string")
```

---

### 
> 

```python
client.v1.game_center_matchmaking_teams.delete(id="string")
```

---

### 
> 

```python
client.v1.in_app_purchase_app_store_review_screenshots.delete(id="string")
```

---

### 
> 

```python
client.v1.in_app_purchase_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.marketplace_domains.delete(id="string")
```

---

### 
> 

```python
client.v1.marketplace_search_details.delete(id="string")
```

---

### 
> 

```python
client.v1.marketplace_webhooks.delete(id="string")
```

---

### 
> 

```python
client.v1.profiles.delete(id="string")
```

---

### 
> 

```python
client.v1.promoted_purchase_images.delete(id="string")
```

---

### 
> 

```python
client.v1.promoted_purchases.delete(id="string")
```

---

### 
> 

```python
client.v1.review_submission_items.delete(id="string")
```

---

### 
> 

```python
client.v1.routing_app_coverages.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_app_store_review_screenshots.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_group_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_groups.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_introductory_offers.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_localizations.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_prices.delete(id="string")
```

---

### 
> 

```python
client.v1.subscription_promotional_offers.delete(id="string")
```

---

### 
> 

```python
client.v1.subscriptions.delete(id="string")
```

---

### 
> 

```python
client.v1.subscriptions.relationships.introductory_offers.delete(
    id="string",
    data={"data": [{"id": "string", "type": "subscriptionIntroductoryOffers"}]},
)
```

---

### 
> 

```python
client.v1.subscriptions.relationships.prices.delete(
    id="string", data={"data": [{"id": "string", "type": "subscriptionPrices"}]}
)
```

---

### 
> 

```python
client.v1.user_invitations.delete(id="string")
```

---

### 
> 

```python
client.v1.users.delete(id="string")
```

---

### 
> 

```python
client.v1.users.relationships.visible_apps.delete(
    id="string", data={"data": [{"id": "string", "type": "apps"}]}
)
```

---

### 
> 

```python
client.v2.app_store_version_experiments.delete(id="string")
```

---

### 
> 

```python
client.v2.in_app_purchases.delete(id="string")
```

---

### 
> 

```python
client.v1.actors.list(filter_id=["string"], fields_actors=["actorType"], limit=123)
```

---

### 
> 

```python
client.v1.actors.get(id="string", fields_actors=["actorType"])
```

---

### 
> 

```python
client.v1.alternative_distribution_domains.list(
    fields_alternative_distribution_domains=["createdDate"], limit=123
)
```

---

### 
> 

```python
client.v1.alternative_distribution_domains.get(
    id="string", fields_alternative_distribution_domains=["createdDate"]
)
```

---

### 
> 

```python
client.v1.alternative_distribution_keys.list(
    exists_app=True, fields_alternative_distribution_keys=["app"], limit=123
)
```

---

### 
> 

```python
client.v1.alternative_distribution_keys.get(
    id="string", fields_alternative_distribution_keys=["app"]
)
```

---

### 
> 

```python
client.v1.alternative_distribution_package_deltas.get(
    id="string",
    fields_alternative_distribution_package_deltas=["alternativeDistributionKeyBlob"],
)
```

---

### 
> 

```python
client.v1.alternative_distribution_package_variants.get(
    id="string",
    fields_alternative_distribution_package_variants=["alternativeDistributionKeyBlob"],
)
```

---

### 
> 

```python
client.v1.alternative_distribution_package_versions.get(
    id="string",
    fields_alternative_distribution_package_deltas=["alternativeDistributionKeyBlob"],
    fields_alternative_distribution_package_variants=["alternativeDistributionKeyBlob"],
    fields_alternative_distribution_package_versions=["alternativeDistributionPackage"],
    include=["alternativeDistributionPackage"],
    limit_deltas=123,
    limit_variants=123,
)
```

---

### 
> 

```python
client.v1.alternative_distribution_package_versions.deltas.list(
    id="string",
    fields_alternative_distribution_package_deltas=["alternativeDistributionKeyBlob"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.alternative_distribution_package_versions.variants.list(
    id="string",
    fields_alternative_distribution_package_variants=["alternativeDistributionKeyBlob"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.alternative_distribution_packages.get(
    id="string",
    fields_alternative_distribution_package_versions=["alternativeDistributionPackage"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    include=["versions"],
    limit_versions=123,
)
```

---

### 
> 

```python
client.v1.alternative_distribution_packages.versions.list(
    id="string",
    fields_alternative_distribution_package_deltas=["alternativeDistributionKeyBlob"],
    fields_alternative_distribution_package_variants=["alternativeDistributionKeyBlob"],
    fields_alternative_distribution_package_versions=["alternativeDistributionPackage"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    filter_state=["COMPLETED"],
    include=["alternativeDistributionPackage"],
    limit=123,
    limit_deltas=123,
    limit_variants=123,
)
```

---

### 
> 

```python
client.v1.analytics_report_instances.get(
    id="string",
    fields_analytics_report_instances=["granularity"],
    fields_analytics_report_segments=["checksum"],
)
```

---

### 
> 

```python
client.v1.analytics_report_instances.segments.list(
    id="string", fields_analytics_report_segments=["checksum"], limit=123
)
```

---

### 
> 

```python
client.v1.analytics_report_requests.get(
    id="string",
    fields_analytics_report_requests=["accessType"],
    fields_analytics_reports=["category"],
    include=["reports"],
    limit_reports=123,
)
```

---

### 
> 

```python
client.v1.analytics_report_requests.reports.list(
    id="string",
    fields_analytics_reports=["category"],
    filter_category=["APP_USAGE"],
    filter_name=["string"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.analytics_report_segments.get(
    id="string", fields_analytics_report_segments=["checksum"]
)
```

---

### 
> 

```python
client.v1.analytics_reports.get(
    id="string",
    fields_analytics_report_instances=["granularity"],
    fields_analytics_reports=["category"],
)
```

---

### 
> 

```python
client.v1.analytics_reports.instances.list(
    id="string",
    fields_analytics_report_instances=["granularity"],
    filter_granularity=["DAILY"],
    filter_processing_date=["string"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_availabilities.get(
    id="string",
    fields_app_availabilities=["app"],
    fields_territories=["currency"],
    include=["app"],
    limit_available_territories=123,
)
```

---

### 
> 

```python
client.v1.app_availabilities.available_territories.list(
    id="string", fields_territories=["currency"], limit=123
)
```

---

### 
> 

```python
client.v1.app_categories.list(
    exists_parent=True,
    fields_app_categories=["parent"],
    filter_platforms=["IOS"],
    include=["parent"],
    limit=123,
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_categories.get(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_categories.parent.list(id="string", fields_app_categories=["parent"])
```

---

### 
> 

```python
client.v1.app_categories.subcategories.list(
    id="string", fields_app_categories=["parent"], limit=123
)
```

---

### 
> 

```python
client.v1.app_clip_advanced_experience_images.get(
    id="string", fields_app_clip_advanced_experience_images=["assetDeliveryState"]
)
```

---

### 
> 

```python
client.v1.app_clip_advanced_experiences.get(
    id="string",
    fields_app_clip_advanced_experiences=["action"],
    include=["appClip"],
    limit_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_clip_app_store_review_details.get(
    id="string",
    fields_app_clip_app_store_review_details=["appClipDefaultExperience"],
    include=["appClipDefaultExperience"],
)
```

---

### 
> 

```python
client.v1.app_clip_default_experience_localizations.get(
    id="string",
    fields_app_clip_default_experience_localizations=["appClipDefaultExperience"],
    fields_app_clip_header_images=["appClipDefaultExperienceLocalization"],
    include=["appClipDefaultExperience"],
)
```

---

### 
> 

```python
client.v1.app_clip_default_experience_localizations.app_clip_header_image.list(
    id="string",
    fields_app_clip_default_experience_localizations=["appClipDefaultExperience"],
    fields_app_clip_header_images=["appClipDefaultExperienceLocalization"],
    include=["appClipDefaultExperienceLocalization"],
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.get(
    id="string",
    fields_app_clip_app_store_review_details=["appClipDefaultExperience"],
    fields_app_clip_default_experience_localizations=["appClipDefaultExperience"],
    fields_app_clip_default_experiences=["action"],
    fields_app_store_versions=["ageRatingDeclaration"],
    include=["appClip"],
    limit_app_clip_default_experience_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.app_clip_app_store_review_detail.list(
    id="string",
    fields_app_clip_app_store_review_details=["appClipDefaultExperience"],
    fields_app_clip_default_experiences=["action"],
    include=["appClipDefaultExperience"],
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.app_clip_default_experience_localizations.list(
    id="string",
    fields_app_clip_default_experience_localizations=["appClipDefaultExperience"],
    fields_app_clip_default_experiences=["action"],
    fields_app_clip_header_images=["appClipDefaultExperienceLocalization"],
    filter_locale=["string"],
    include=["appClipDefaultExperience"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.relationships.release_with_app_store_version.list(
    id="string"
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.release_with_app_store_version.list(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    fields_app_clip_default_experiences=["action"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_version_localizations=["appPreviewSets"],
    fields_app_store_version_phased_releases=["appStoreVersion"],
    fields_app_store_version_submissions=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    fields_routing_app_coverages=["appStoreVersion"],
    include=["ageRatingDeclaration"],
    limit_app_store_version_experiments_v2=123,
    limit_app_store_version_experiments=123,
    limit_app_store_version_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_clip_header_images.get(
    id="string",
    fields_app_clip_header_images=["appClipDefaultExperienceLocalization"],
    include=["appClipDefaultExperienceLocalization"],
)
```

---

### 
> 

```python
client.v1.app_clips.get(
    id="string",
    fields_app_clip_advanced_experiences=["action"],
    fields_app_clip_default_experiences=["action"],
    fields_app_clips=["app"],
    include=["app"],
    limit_app_clip_default_experiences=123,
)
```

---

### 
> 

```python
client.v1.app_clips.app_clip_advanced_experiences.list(
    id="string",
    fields_app_clip_advanced_experience_images=["assetDeliveryState"],
    fields_app_clip_advanced_experience_localizations=["language"],
    fields_app_clip_advanced_experiences=["action"],
    fields_app_clips=["app"],
    filter_action=["OPEN"],
    filter_place_status=["PENDING"],
    filter_status=["RECEIVED"],
    include=["appClip"],
    limit=123,
    limit_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_clips.app_clip_default_experiences.list(
    id="string",
    exists_release_with_app_store_version=True,
    fields_app_clip_app_store_review_details=["appClipDefaultExperience"],
    fields_app_clip_default_experience_localizations=["appClipDefaultExperience"],
    fields_app_clip_default_experiences=["action"],
    fields_app_clips=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    include=["appClip"],
    limit=123,
    limit_app_clip_default_experience_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_localizations.get(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    include=["appCustomProductPageVersion"],
    limit_app_preview_sets=123,
    limit_app_screenshot_sets=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_localizations.app_preview_sets.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_previews=["appPreviewSet"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_localizations=["appPreviewSets"],
    filter_app_store_version_experiment_treatment_localization=["string"],
    filter_app_store_version_localization=["string"],
    filter_preview_type=["IPHONE_67"],
    include=["appCustomProductPageLocalization"],
    limit=123,
    limit_app_previews=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_localizations.app_screenshot_sets.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_screenshots=["appScreenshotSet"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_localizations=["appPreviewSets"],
    filter_app_store_version_experiment_treatment_localization=["string"],
    filter_app_store_version_localization=["string"],
    filter_screenshot_display_type=["APP_IPHONE_67"],
    include=["appCustomProductPageLocalization"],
    limit=123,
    limit_app_screenshots=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_versions.get(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_custom_product_page_versions=["appCustomProductPage"],
    include=["appCustomProductPage"],
    limit_app_custom_product_page_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_versions.app_custom_product_page_localizations.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_custom_product_page_versions=["appCustomProductPage"],
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    filter_locale=["string"],
    include=["appCustomProductPageVersion"],
    limit=123,
    limit_app_preview_sets=123,
    limit_app_screenshot_sets=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_pages.get(
    id="string",
    fields_app_custom_product_page_versions=["appCustomProductPage"],
    fields_app_custom_product_pages=["app"],
    include=["app"],
    limit_app_custom_product_page_versions=123,
)
```

---

### 
> 

```python
client.v1.app_custom_product_pages.app_custom_product_page_versions.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_custom_product_page_versions=["appCustomProductPage"],
    fields_app_custom_product_pages=["app"],
    filter_state=["PREPARE_FOR_SUBMISSION"],
    include=["appCustomProductPage"],
    limit=123,
    limit_app_custom_product_page_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_encryption_declaration_documents.get(
    id="string",
    fields_app_encryption_declaration_documents=["appEncryptionDeclaration"],
)
```

---

### 
> 

```python
client.v1.app_encryption_declarations.list(
    fields_app_encryption_declaration_documents=["appEncryptionDeclaration"],
    fields_app_encryption_declarations=["app"],
    fields_apps=["alternativeDistributionKey"],
    filter_app=["string"],
    filter_builds=["string"],
    filter_platform=["IOS"],
    include=["app"],
    limit=123,
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.app_encryption_declarations.get(
    id="string",
    fields_app_encryption_declaration_documents=["appEncryptionDeclaration"],
    fields_app_encryption_declarations=["app"],
    fields_apps=["alternativeDistributionKey"],
    include=["app"],
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.app_encryption_declarations.app.list(
    id="string", fields_apps=["alternativeDistributionKey"]
)
```

---

### 
> 

```python
client.v1.app_encryption_declarations.app_encryption_declaration_document.list(
    id="string",
    fields_app_encryption_declaration_documents=["appEncryptionDeclaration"],
)
```

---

### 
> 

```python
client.v1.app_event_localizations.get(
    id="string",
    fields_app_event_localizations=["appEvent"],
    fields_app_event_screenshots=["appEventAssetType"],
    fields_app_event_video_clips=["appEventAssetType"],
    include=["appEvent"],
    limit_app_event_screenshots=123,
    limit_app_event_video_clips=123,
)
```

---

### 
> 

```python
client.v1.app_event_localizations.app_event_screenshots.list(
    id="string",
    fields_app_event_localizations=["appEvent"],
    fields_app_event_screenshots=["appEventAssetType"],
    include=["appEventLocalization"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_event_localizations.app_event_video_clips.list(
    id="string",
    fields_app_event_localizations=["appEvent"],
    fields_app_event_video_clips=["appEventAssetType"],
    include=["appEventLocalization"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_event_screenshots.get(
    id="string",
    fields_app_event_screenshots=["appEventAssetType"],
    include=["appEventLocalization"],
)
```

---

### 
> 

```python
client.v1.app_event_video_clips.get(
    id="string",
    fields_app_event_video_clips=["appEventAssetType"],
    include=["appEventLocalization"],
)
```

---

### 
> 

```python
client.v1.app_events.get(
    id="string",
    fields_app_event_localizations=["appEvent"],
    fields_app_events=["app"],
    include=["localizations"],
    limit_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_events.localizations.list(
    id="string",
    fields_app_event_localizations=["appEvent"],
    fields_app_event_screenshots=["appEventAssetType"],
    fields_app_event_video_clips=["appEventAssetType"],
    fields_app_events=["app"],
    include=["appEvent"],
    limit=123,
    limit_app_event_screenshots=123,
    limit_app_event_video_clips=123,
)
```

---

### 
> 

```python
client.v1.app_info_localizations.get(
    id="string", fields_app_info_localizations=["appInfo"], include=["appInfo"]
)
```

---

### 
> 

```python
client.v1.app_infos.get(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_app_categories=["parent"],
    fields_app_info_localizations=["appInfo"],
    fields_app_infos=["ageRatingDeclaration"],
    include=["ageRatingDeclaration"],
    limit_app_info_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_infos.age_rating_declaration.list(
    id="string", fields_age_rating_declarations=["ageRatingOverride"]
)
```

---

### 
> 

```python
client.v1.app_infos.app_info_localizations.list(
    id="string",
    fields_app_info_localizations=["appInfo"],
    fields_app_infos=["ageRatingDeclaration"],
    filter_locale=["string"],
    include=["appInfo"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_infos.primary_category.list(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_infos.primary_subcategory_one.list(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_infos.primary_subcategory_two.list(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_infos.secondary_category.list(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_infos.secondary_subcategory_one.list(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_infos.secondary_subcategory_two.list(
    id="string",
    fields_app_categories=["parent"],
    include=["parent"],
    limit_subcategories=123,
)
```

---

### 
> 

```python
client.v1.app_pre_orders.get(
    id="string", fields_app_pre_orders=["app"], include=["app"]
)
```

---

### 
> 

```python
client.v1.app_preview_sets.get(
    id="string",
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_previews=["appPreviewSet"],
    include=["appCustomProductPageLocalization"],
    limit_app_previews=123,
)
```

---

### 
> 

```python
client.v1.app_preview_sets.app_previews.list(
    id="string",
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_previews=["appPreviewSet"],
    include=["appPreviewSet"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_preview_sets.relationships.app_previews.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.app_previews.get(
    id="string", fields_app_previews=["appPreviewSet"], include=["appPreviewSet"]
)
```

---

### 
> 

```python
client.v1.app_price_schedules.get(
    id="string",
    fields_app_price_schedules=["app"],
    fields_app_prices=["appPricePoint"],
    fields_territories=["currency"],
    include=["app"],
    limit_automatic_prices=123,
    limit_manual_prices=123,
)
```

---

### 
> 

```python
client.v1.app_price_schedules.automatic_prices.list(
    id="string",
    fields_app_price_points=["app"],
    fields_app_prices=["appPricePoint"],
    fields_territories=["currency"],
    filter_end_date=["string"],
    filter_start_date=["string"],
    filter_territory=["string"],
    include=["appPricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_price_schedules.base_territory.list(
    id="string", fields_territories=["currency"]
)
```

---

### 
> 

```python
client.v1.app_price_schedules.manual_prices.list(
    id="string",
    fields_app_price_points=["app"],
    fields_app_prices=["appPricePoint"],
    fields_territories=["currency"],
    filter_end_date=["string"],
    filter_start_date=["string"],
    filter_territory=["string"],
    include=["appPricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_screenshot_sets.get(
    id="string",
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_screenshots=["appScreenshotSet"],
    include=["appCustomProductPageLocalization"],
    limit_app_screenshots=123,
)
```

---

### 
> 

```python
client.v1.app_screenshot_sets.app_screenshots.list(
    id="string",
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_screenshots=["appScreenshotSet"],
    include=["appScreenshotSet"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_screenshot_sets.relationships.app_screenshots.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.app_screenshots.get(
    id="string",
    fields_app_screenshots=["appScreenshotSet"],
    include=["appScreenshotSet"],
)
```

---

### 
> 

```python
client.v1.app_store_review_attachments.get(
    id="string",
    fields_app_store_review_attachments=["appStoreReviewDetail"],
    include=["appStoreReviewDetail"],
)
```

---

### 
> 

```python
client.v1.app_store_review_details.get(
    id="string",
    fields_app_store_review_attachments=["appStoreReviewDetail"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    include=["appStoreReviewAttachments"],
    limit_app_store_review_attachments=123,
)
```

---

### 
> 

```python
client.v1.app_store_review_details.app_store_review_attachments.list(
    id="string",
    fields_app_store_review_attachments=["appStoreReviewDetail"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    include=["appStoreReviewDetail"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatment_localizations.get(
    id="string",
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    include=["appPreviewSets"],
    limit_app_preview_sets=123,
    limit_app_screenshot_sets=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatment_localizations.app_preview_sets.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_previews=["appPreviewSet"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_localizations=["appPreviewSets"],
    filter_app_custom_product_page_localization=["string"],
    filter_app_store_version_localization=["string"],
    filter_preview_type=["IPHONE_67"],
    include=["appCustomProductPageLocalization"],
    limit=123,
    limit_app_previews=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatment_localizations.app_screenshot_sets.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_screenshots=["appScreenshotSet"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_localizations=["appPreviewSets"],
    filter_app_custom_product_page_localization=["string"],
    filter_app_store_version_localization=["string"],
    filter_screenshot_display_type=["APP_IPHONE_67"],
    include=["appCustomProductPageLocalization"],
    limit=123,
    limit_app_screenshots=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatments.get(
    id="string",
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_experiment_treatments=["appIcon"],
    include=["appStoreVersionExperiment"],
    limit_app_store_version_experiment_treatment_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatments.app_store_version_experiment_treatment_localizations.list(
    id="string",
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_experiment_treatments=["appIcon"],
    filter_locale=["string"],
    include=["appPreviewSets"],
    limit=123,
    limit_app_preview_sets=123,
    limit_app_screenshot_sets=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiments.get(
    id="string",
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["appStoreVersion"],
    include=["appStoreVersion"],
    limit_app_store_version_experiment_treatments=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_experiments.app_store_version_experiment_treatments.list(
    id="string",
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["app"],
    include=["appStoreVersionExperiment"],
    limit=123,
    limit_app_store_version_experiment_treatment_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_localizations.get(
    id="string",
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_store_version_localizations=["appPreviewSets"],
    include=["appPreviewSets"],
    limit_app_preview_sets=123,
    limit_app_screenshot_sets=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_localizations.app_preview_sets.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_previews=["appPreviewSet"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_localizations=["appPreviewSets"],
    filter_app_custom_product_page_localization=["string"],
    filter_app_store_version_experiment_treatment_localization=["string"],
    filter_preview_type=["IPHONE_67"],
    include=["appCustomProductPageLocalization"],
    limit=123,
    limit_app_previews=123,
)
```

---

### 
> 

```python
client.v1.app_store_version_localizations.app_screenshot_sets.list(
    id="string",
    fields_app_custom_product_page_localizations=["appCustomProductPageVersion"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_screenshots=["appScreenshotSet"],
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_localizations=["appPreviewSets"],
    filter_app_custom_product_page_localization=["string"],
    filter_app_store_version_experiment_treatment_localization=["string"],
    filter_screenshot_display_type=["APP_IPHONE_67"],
    include=["appCustomProductPageLocalization"],
    limit=123,
    limit_app_screenshots=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.get(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    fields_app_clip_default_experiences=["action"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_version_localizations=["appPreviewSets"],
    fields_app_store_version_phased_releases=["appStoreVersion"],
    fields_app_store_version_submissions=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_builds=["app"],
    fields_customer_reviews=["body"],
    fields_routing_app_coverages=["appStoreVersion"],
    include=["ageRatingDeclaration"],
    limit_app_store_version_experiments_v2=123,
    limit_app_store_version_experiments=123,
    limit_app_store_version_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.age_rating_declaration.list(
    id="string", fields_age_rating_declarations=["ageRatingOverride"]
)
```

---

### 
> 

```python
client.v1.app_store_versions.alternative_distribution_package.list(
    id="string",
    fields_alternative_distribution_package_versions=["alternativeDistributionPackage"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    include=["versions"],
    limit_versions=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_clip_default_experience.list(
    id="string",
    fields_app_clip_app_store_review_details=["appClipDefaultExperience"],
    fields_app_clip_default_experience_localizations=["appClipDefaultExperience"],
    fields_app_clip_default_experiences=["action"],
    fields_app_clips=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    include=["appClip"],
    limit_app_clip_default_experience_localizations=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_store_review_detail.list(
    id="string",
    fields_app_store_review_attachments=["appStoreReviewDetail"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    fields_app_store_versions=["ageRatingDeclaration"],
    include=["appStoreReviewAttachments"],
    limit_app_store_review_attachments=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_store_version_experiments.list(
    id="string",
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    filter_state=["PREPARE_FOR_SUBMISSION"],
    include=["appStoreVersion"],
    limit=123,
    limit_app_store_version_experiment_treatments=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_store_version_experiments_v2.list(
    id="string",
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    filter_state=["PREPARE_FOR_SUBMISSION"],
    include=["app"],
    limit=123,
    limit_app_store_version_experiment_treatments=123,
    limit_control_versions=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_store_version_localizations.list(
    id="string",
    fields_app_preview_sets=["appCustomProductPageLocalization"],
    fields_app_screenshot_sets=["appCustomProductPageLocalization"],
    fields_app_store_version_localizations=["appPreviewSets"],
    fields_app_store_versions=["ageRatingDeclaration"],
    filter_locale=["string"],
    include=["appPreviewSets"],
    limit=123,
    limit_app_preview_sets=123,
    limit_app_screenshot_sets=123,
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_store_version_phased_release.list(
    id="string", fields_app_store_version_phased_releases=["appStoreVersion"]
)
```

---

### 
> 

```python
client.v1.app_store_versions.app_store_version_submission.list(
    id="string",
    fields_app_store_version_submissions=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    include=["appStoreVersion"],
)
```

---

### 
> 

```python
client.v1.app_store_versions.build.list(id="string", fields_builds=["app"])
```

---

### 
> 

```python
client.v1.app_store_versions.customer_reviews.list(
    id="string",
    exists_published_response=True,
    fields_customer_review_responses=["lastModifiedDate"],
    fields_customer_reviews=["body"],
    filter_rating=["string"],
    filter_territory=["ABW"],
    include=["response"],
    limit=123,
    sort=["createdDate"],
)
```

---

### 
> 

```python
client.v1.app_store_versions.relationships.app_clip_default_experience.list(id="string")
```

---

### 
> 

```python
client.v1.app_store_versions.relationships.build.list(id="string")
```

---

### 
> 

```python
client.v1.app_store_versions.routing_app_coverage.list(
    id="string", fields_routing_app_coverages=["appStoreVersion"]
)
```

---

### 
> 

```python
client.v1.apps.list(
    exists_game_center_enabled_versions=True,
    fields_alternative_distribution_keys=["app"],
    fields_analytics_report_requests=["accessType"],
    fields_app_availabilities=["app"],
    fields_app_clips=["app"],
    fields_app_custom_product_pages=["app"],
    fields_app_encryption_declarations=["app"],
    fields_app_events=["app"],
    fields_app_infos=["ageRatingDeclaration"],
    fields_app_pre_orders=["app"],
    fields_app_price_points=["app"],
    fields_app_price_schedules=["app"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_localizations=["app"],
    fields_beta_app_review_details=["app"],
    fields_beta_groups=["app"],
    fields_beta_license_agreements=["agreementText"],
    fields_builds=["app"],
    fields_ci_products=["additionalRepositories"],
    fields_customer_reviews=["body"],
    fields_end_user_license_agreements=["agreementText"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_enabled_versions=["app"],
    fields_in_app_purchases=["app"],
    fields_marketplace_search_details=["app"],
    fields_perf_power_metrics=["deviceType"],
    fields_pre_release_versions=["app"],
    fields_promoted_purchases=["app"],
    fields_review_submissions=["app"],
    fields_subscription_grace_periods=["duration"],
    fields_subscription_groups=["app"],
    filter_app_store_versions_app_store_state=["ACCEPTED"],
    filter_app_store_versions_app_version_state=["ACCEPTED"],
    filter_app_store_versions_platform=["IOS"],
    filter_app_store_versions=["string"],
    filter_bundle_id=["string"],
    filter_id=["string"],
    filter_name=["string"],
    filter_sku=["string"],
    include=["appClips"],
    limit=123,
    limit_app_clips=123,
    limit_app_custom_product_pages=123,
    limit_app_encryption_declarations=123,
    limit_app_events=123,
    limit_app_infos=123,
    limit_app_store_version_experiments_v2=123,
    limit_app_store_versions=123,
    limit_beta_app_localizations=123,
    limit_beta_groups=123,
    limit_builds=123,
    limit_game_center_enabled_versions=123,
    limit_in_app_purchases_v2=123,
    limit_in_app_purchases=123,
    limit_pre_release_versions=123,
    limit_promoted_purchases=123,
    limit_review_submissions=123,
    limit_subscription_groups=123,
    sort=["bundleId"],
)
```

---

### 
> 

```python
client.v1.apps.get(
    id="string",
    fields_alternative_distribution_keys=["app"],
    fields_analytics_report_requests=["accessType"],
    fields_app_availabilities=["app"],
    fields_app_clips=["app"],
    fields_app_custom_product_pages=["app"],
    fields_app_encryption_declarations=["app"],
    fields_app_events=["app"],
    fields_app_infos=["ageRatingDeclaration"],
    fields_app_pre_orders=["app"],
    fields_app_price_points=["app"],
    fields_app_price_schedules=["app"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_localizations=["app"],
    fields_beta_app_review_details=["app"],
    fields_beta_groups=["app"],
    fields_beta_license_agreements=["agreementText"],
    fields_builds=["app"],
    fields_ci_products=["additionalRepositories"],
    fields_customer_reviews=["body"],
    fields_end_user_license_agreements=["agreementText"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_enabled_versions=["app"],
    fields_in_app_purchases=["app"],
    fields_marketplace_search_details=["app"],
    fields_perf_power_metrics=["deviceType"],
    fields_pre_release_versions=["app"],
    fields_promoted_purchases=["app"],
    fields_review_submissions=["app"],
    fields_subscription_grace_periods=["duration"],
    fields_subscription_groups=["app"],
    include=["appClips"],
    limit_app_clips=123,
    limit_app_custom_product_pages=123,
    limit_app_encryption_declarations=123,
    limit_app_events=123,
    limit_app_infos=123,
    limit_app_store_version_experiments_v2=123,
    limit_app_store_versions=123,
    limit_beta_app_localizations=123,
    limit_beta_groups=123,
    limit_builds=123,
    limit_game_center_enabled_versions=123,
    limit_in_app_purchases_v2=123,
    limit_in_app_purchases=123,
    limit_pre_release_versions=123,
    limit_promoted_purchases=123,
    limit_review_submissions=123,
    limit_subscription_groups=123,
)
```

---

### 
> 

```python
client.v1.apps.alternative_distribution_key.list(
    id="string", fields_alternative_distribution_keys=["app"]
)
```

---

### 
> 

```python
client.v1.apps.analytics_report_requests.list(
    id="string",
    fields_analytics_report_requests=["accessType"],
    fields_analytics_reports=["category"],
    filter_access_type=["ONE_TIME_SNAPSHOT"],
    include=["reports"],
    limit=123,
    limit_reports=123,
)
```

---

### 
> 

```python
client.v1.apps.app_availability.list(
    id="string",
    fields_app_availabilities=["app"],
    fields_apps=["alternativeDistributionKey"],
    fields_territories=["currency"],
    include=["app"],
    limit_available_territories=123,
)
```

---

### 
> 

```python
client.v1.apps.app_clips.list(
    id="string",
    fields_app_clip_default_experiences=["action"],
    fields_app_clips=["app"],
    fields_apps=["alternativeDistributionKey"],
    filter_bundle_id=["string"],
    include=["app"],
    limit=123,
    limit_app_clip_default_experiences=123,
)
```

---

### 
> 

```python
client.v1.apps.app_custom_product_pages.list(
    id="string",
    fields_app_custom_product_page_versions=["appCustomProductPage"],
    fields_app_custom_product_pages=["app"],
    fields_apps=["alternativeDistributionKey"],
    filter_visible=["string"],
    include=["app"],
    limit=123,
    limit_app_custom_product_page_versions=123,
)
```

---

### 
> 

```python
client.v1.apps.app_encryption_declarations.list(
    id="string",
    fields_app_encryption_declaration_documents=["appEncryptionDeclaration"],
    fields_app_encryption_declarations=["app"],
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    filter_builds=["string"],
    filter_platform=["IOS"],
    include=["app"],
    limit=123,
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.apps.app_events.list(
    id="string",
    fields_app_event_localizations=["appEvent"],
    fields_app_events=["app"],
    filter_event_state=["DRAFT"],
    filter_id=["string"],
    include=["localizations"],
    limit=123,
    limit_localizations=123,
)
```

---

### 
> 

```python
client.v1.apps.app_infos.list(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_app_categories=["parent"],
    fields_app_info_localizations=["appInfo"],
    fields_app_infos=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    include=["ageRatingDeclaration"],
    limit=123,
    limit_app_info_localizations=123,
)
```

---

### 
> 

```python
client.v1.apps.app_price_points.list(
    id="string",
    fields_app_price_points=["app"],
    fields_apps=["alternativeDistributionKey"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["app"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.apps.app_price_schedule.list(
    id="string",
    fields_app_price_schedules=["app"],
    fields_app_prices=["appPricePoint"],
    fields_apps=["alternativeDistributionKey"],
    fields_territories=["currency"],
    include=["app"],
    limit_automatic_prices=123,
    limit_manual_prices=123,
)
```

---

### 
> 

```python
client.v1.apps.app_store_version_experiments_v2.list(
    id="string",
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    filter_state=["PREPARE_FOR_SUBMISSION"],
    include=["app"],
    limit=123,
    limit_app_store_version_experiment_treatments=123,
    limit_control_versions=123,
)
```

---

### 
> 

```python
client.v1.apps.app_store_versions.list(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    fields_app_clip_default_experiences=["action"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_version_localizations=["appPreviewSets"],
    fields_app_store_version_phased_releases=["appStoreVersion"],
    fields_app_store_version_submissions=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    fields_routing_app_coverages=["appStoreVersion"],
    filter_app_store_state=["ACCEPTED"],
    filter_app_version_state=["ACCEPTED"],
    filter_id=["string"],
    filter_platform=["IOS"],
    filter_version_string=["string"],
    include=["ageRatingDeclaration"],
    limit=123,
    limit_app_store_version_experiments_v2=123,
    limit_app_store_version_experiments=123,
    limit_app_store_version_localizations=123,
)
```

---

### 
> 

```python
client.v1.apps.beta_app_localizations.list(
    id="string", fields_beta_app_localizations=["app"], limit=123
)
```

---

### 
> 

```python
client.v1.apps.beta_app_review_detail.list(
    id="string", fields_beta_app_review_details=["app"]
)
```

---

### 
> 

```python
client.v1.apps.beta_groups.list(id="string", fields_beta_groups=["app"], limit=123)
```

---

### 
> 

```python
client.v1.apps.beta_license_agreement.list(
    id="string", fields_beta_license_agreements=["agreementText"]
)
```

---

### 
> 

```python
client.v1.apps.builds.list(id="string", fields_builds=["app"], limit=123)
```

---

### 
> 

```python
client.v1.apps.ci_product.list(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_bundle_ids=["app"],
    fields_ci_products=["additionalRepositories"],
    fields_scm_repositories=["defaultBranch"],
    include=["app"],
    limit_primary_repositories=123,
)
```

---

### 
> 

```python
client.v1.apps.customer_reviews.list(
    id="string",
    exists_published_response=True,
    fields_customer_review_responses=["lastModifiedDate"],
    fields_customer_reviews=["body"],
    filter_rating=["string"],
    filter_territory=["ABW"],
    include=["response"],
    limit=123,
    sort=["createdDate"],
)
```

---

### 
> 

```python
client.v1.apps.end_user_license_agreement.list(
    id="string", fields_end_user_license_agreements=["agreementText"]
)
```

---

### 
> 

```python
client.v1.apps.game_center_detail.list(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_app_versions=["appStoreVersion"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["achievementReleases"],
    limit_achievement_releases=123,
    limit_game_center_achievements=123,
    limit_game_center_app_versions=123,
    limit_game_center_leaderboard_sets=123,
    limit_game_center_leaderboards=123,
    limit_leaderboard_releases=123,
    limit_leaderboard_set_releases=123,
)
```

---

### 
> 

```python
client.v1.apps.game_center_enabled_versions.list(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_game_center_enabled_versions=["app"],
    filter_id=["string"],
    filter_platform=["IOS"],
    filter_version_string=["string"],
    include=["app"],
    limit=123,
    limit_compatible_versions=123,
    sort=["versionString"],
)
```

---

### 
> 

```python
client.v1.apps.in_app_purchases.list(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_in_app_purchases=["apps"],
    filter_can_be_submitted=["string"],
    filter_in_app_purchase_type=["AUTOMATICALLY_RENEWABLE_SUBSCRIPTION"],
    include=["apps"],
    limit=123,
    limit_apps=123,
    sort=["inAppPurchaseType"],
)
```

---

### 
> 

```python
client.v1.apps.in_app_purchases_v2.list(
    id="string",
    fields_in_app_purchase_app_store_review_screenshots=["assetDeliveryState"],
    fields_in_app_purchase_availabilities=["availableInNewTerritories"],
    fields_in_app_purchase_contents=["fileName"],
    fields_in_app_purchase_localizations=["description"],
    fields_in_app_purchase_price_schedules=["automaticPrices"],
    fields_in_app_purchases=["app"],
    fields_promoted_purchases=["app"],
    filter_in_app_purchase_type=["CONSUMABLE"],
    filter_name=["string"],
    filter_product_id=["string"],
    filter_state=["MISSING_METADATA"],
    include=["appStoreReviewScreenshot"],
    limit=123,
    limit_in_app_purchase_localizations=123,
    sort=["inAppPurchaseType"],
)
```

---

### 
> 

```python
client.v1.apps.marketplace_search_detail.list(
    id="string", fields_marketplace_search_details=["app"]
)
```

---

### 
> 

```python
client.v1.apps.metrics.beta_tester_usages.list(
    id="string",
    filter_beta_testers="string",
    group_by=["betaTesters"],
    limit=123,
    period="P7D",
)
```

---

### 
> 

```python
client.v1.apps.perf_power_metrics.list(
    id="string",
    filter_device_type=["string"],
    filter_metric_type=["DISK"],
    filter_platform=["IOS"],
)
```

---

### 
> 

```python
client.v1.apps.pre_order.list(id="string", fields_app_pre_orders=["app"])
```

---

### 
> 

```python
client.v1.apps.pre_release_versions.list(
    id="string", fields_pre_release_versions=["app"], limit=123
)
```

---

### 
> 

```python
client.v1.apps.promoted_purchases.list(
    id="string",
    fields_in_app_purchases=["app"],
    fields_promoted_purchase_images=["assetToken"],
    fields_promoted_purchases=["app"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["inAppPurchaseV2"],
    limit=123,
    limit_promotion_images=123,
)
```

---

### 
> 

```python
client.v1.apps.relationships.promoted_purchases.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.apps.review_submissions.list(
    id="string",
    fields_actors=["actorType"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_review_submission_items=["appCustomProductPageVersion"],
    fields_review_submissions=["app"],
    filter_platform=["IOS"],
    filter_state=["READY_FOR_REVIEW"],
    include=["app"],
    limit=123,
    limit_items=123,
)
```

---

### 
> 

```python
client.v1.apps.subscription_grace_period.list(
    id="string", fields_subscription_grace_periods=["duration"]
)
```

---

### 
> 

```python
client.v1.apps.subscription_groups.list(
    id="string",
    fields_subscription_group_localizations=["customAppName"],
    fields_subscription_groups=["app"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    filter_reference_name=["string"],
    filter_subscriptions_state=["MISSING_METADATA"],
    include=["subscriptionGroupLocalizations"],
    limit=123,
    limit_subscription_group_localizations=123,
    limit_subscriptions=123,
    sort=["referenceName"],
)
```

---

### 
> 

```python
client.v1.beta_app_clip_invocations.get(
    id="string",
    fields_beta_app_clip_invocations=["betaAppClipInvocationLocalizations"],
    include=["betaAppClipInvocationLocalizations"],
    limit_beta_app_clip_invocation_localizations=123,
)
```

---

### 
> 

```python
client.v1.beta_app_localizations.list(
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_localizations=["app"],
    filter_app=["string"],
    filter_locale=["string"],
    include=["app"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.beta_app_localizations.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_localizations=["app"],
    include=["app"],
)
```

---

### 
> 

```python
client.v1.beta_app_localizations.app.list(
    id="string", fields_apps=["alternativeDistributionKey"]
)
```

---

### 
> 

```python
client.v1.beta_app_review_details.list(
    filter_app=["string"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_review_details=["app"],
    include=["app"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.beta_app_review_details.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_review_details=["app"],
    include=["app"],
)
```

---

### 
> 

```python
client.v1.beta_app_review_details.app.list(
    id="string", fields_apps=["alternativeDistributionKey"]
)
```

---

### 
> 

```python
client.v1.beta_app_review_submissions.list(
    filter_build=["string"],
    fields_beta_app_review_submissions=["betaReviewState"],
    fields_builds=["app"],
    filter_beta_review_state=["WAITING_FOR_REVIEW"],
    include=["build"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.beta_app_review_submissions.get(
    id="string",
    fields_beta_app_review_submissions=["betaReviewState"],
    fields_builds=["app"],
    include=["build"],
)
```

---

### 
> 

```python
client.v1.beta_app_review_submissions.build.list(id="string", fields_builds=["app"])
```

---

### 
> 

```python
client.v1.beta_build_localizations.list(
    fields_beta_build_localizations=["build"],
    fields_builds=["app"],
    filter_build=["string"],
    filter_locale=["string"],
    include=["build"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.beta_build_localizations.get(
    id="string",
    fields_beta_build_localizations=["build"],
    fields_builds=["app"],
    include=["build"],
)
```

---

### 
> 

```python
client.v1.beta_build_localizations.build.list(id="string", fields_builds=["app"])
```

---

### 
> 

```python
client.v1.beta_groups.list(
    fields_apps=["alternativeDistributionKey"],
    fields_beta_groups=["app"],
    fields_beta_testers=["apps"],
    fields_builds=["app"],
    filter_app=["string"],
    filter_builds=["string"],
    filter_id=["string"],
    filter_is_internal_group=["string"],
    filter_name=["string"],
    filter_public_link_enabled=["string"],
    filter_public_link_limit_enabled=["string"],
    filter_public_link=["string"],
    include=["app"],
    limit=123,
    limit_beta_testers=123,
    limit_builds=123,
    sort=["createdDate"],
)
```

---

### 
> 

```python
client.v1.beta_groups.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_beta_groups=["app"],
    fields_beta_testers=["apps"],
    fields_builds=["app"],
    include=["app"],
    limit_beta_testers=123,
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.beta_groups.app.list(id="string", fields_apps=["alternativeDistributionKey"])
```

---

### 
> 

```python
client.v1.beta_groups.beta_testers.list(
    id="string", fields_beta_testers=["apps"], limit=123
)
```

---

### 
> 

```python
client.v1.beta_groups.builds.list(id="string", fields_builds=["app"], limit=123)
```

---

### 
> 

```python
client.v1.beta_groups.metrics.beta_tester_usages.list(
    id="string",
    filter_beta_testers="string",
    group_by=["betaTesters"],
    limit=123,
    period="P7D",
)
```

---

### 
> 

```python
client.v1.beta_groups.relationships.beta_testers.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.beta_groups.relationships.builds.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.beta_license_agreements.list(
    fields_apps=["alternativeDistributionKey"],
    fields_beta_license_agreements=["agreementText"],
    filter_app=["string"],
    include=["app"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.beta_license_agreements.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_beta_license_agreements=["agreementText"],
    include=["app"],
)
```

---

### 
> 

```python
client.v1.beta_license_agreements.app.list(
    id="string", fields_apps=["alternativeDistributionKey"]
)
```

---

### 
> 

```python
client.v1.beta_testers.list(
    fields_apps=["alternativeDistributionKey"],
    fields_beta_groups=["app"],
    fields_beta_testers=["apps"],
    fields_builds=["app"],
    filter_apps=["string"],
    filter_beta_groups=["string"],
    filter_builds=["string"],
    filter_email=["string"],
    filter_first_name=["string"],
    filter_id=["string"],
    filter_invite_type=["EMAIL"],
    filter_last_name=["string"],
    include=["apps"],
    limit=123,
    limit_apps=123,
    limit_beta_groups=123,
    limit_builds=123,
    sort=["email"],
)
```

---

### 
> 

```python
client.v1.beta_testers.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_beta_groups=["app"],
    fields_beta_testers=["apps"],
    fields_builds=["app"],
    include=["apps"],
    limit_apps=123,
    limit_beta_groups=123,
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.beta_testers.apps.list(
    id="string", fields_apps=["alternativeDistributionKey"], limit=123
)
```

---

### 
> 

```python
client.v1.beta_testers.beta_groups.list(
    id="string", fields_beta_groups=["app"], limit=123
)
```

---

### 
> 

```python
client.v1.beta_testers.builds.list(id="string", fields_builds=["app"], limit=123)
```

---

### 
> 

```python
client.v1.beta_testers.metrics.beta_tester_usages.list(
    id="string", filter_apps="string", limit=123, period="P7D"
)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.apps.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.beta_groups.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.builds.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.build_beta_details.list(
    fields_build_beta_details=["autoNotifyEnabled"],
    fields_builds=["app"],
    filter_build=["string"],
    filter_id=["string"],
    include=["build"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.build_beta_details.get(
    id="string",
    fields_build_beta_details=["autoNotifyEnabled"],
    fields_builds=["app"],
    include=["build"],
)
```

---

### 
> 

```python
client.v1.build_beta_details.build.list(id="string", fields_builds=["app"])
```

---

### 
> 

```python
client.v1.build_bundles.app_clip_domain_cache_status.list(
    id="string", fields_app_clip_domain_statuses=["domains"]
)
```

---

### 
> 

```python
client.v1.build_bundles.app_clip_domain_debug_status.list(
    id="string", fields_app_clip_domain_statuses=["domains"]
)
```

---

### 
> 

```python
client.v1.build_bundles.beta_app_clip_invocations.list(
    id="string",
    fields_beta_app_clip_invocation_localizations=["betaAppClipInvocation"],
    fields_beta_app_clip_invocations=["betaAppClipInvocationLocalizations"],
    include=["betaAppClipInvocationLocalizations"],
    limit=123,
    limit_beta_app_clip_invocation_localizations=123,
)
```

---

### 
> 

```python
client.v1.build_bundles.build_bundle_file_sizes.list(
    id="string", fields_build_bundle_file_sizes=["deviceModel"], limit=123
)
```

---

### 
> 

```python
client.v1.builds.list(
    fields_app_encryption_declarations=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_review_submissions=["betaReviewState"],
    fields_beta_build_localizations=["build"],
    fields_beta_testers=["apps"],
    fields_build_beta_details=["autoNotifyEnabled"],
    fields_build_icons=["iconAsset"],
    fields_builds=["app"],
    fields_diagnostic_signatures=["diagnosticType"],
    fields_perf_power_metrics=["deviceType"],
    fields_pre_release_versions=["app"],
    filter_app_store_version=["string"],
    filter_app=["string"],
    filter_beta_app_review_submission_beta_review_state=["WAITING_FOR_REVIEW"],
    filter_beta_groups=["string"],
    filter_build_audience_type=["INTERNAL_ONLY"],
    filter_expired=["string"],
    filter_id=["string"],
    filter_pre_release_version_platform=["IOS"],
    filter_pre_release_version_version=["string"],
    filter_pre_release_version=["string"],
    filter_processing_state=["PROCESSING"],
    filter_uses_non_exempt_encryption=["string"],
    filter_version=["string"],
    include=["app"],
    limit=123,
    limit_beta_build_localizations=123,
    limit_beta_groups=123,
    limit_build_bundles=123,
    limit_icons=123,
    limit_individual_testers=123,
    sort=["preReleaseVersion"],
)
```

---

### 
> 

```python
client.v1.builds.get(
    id="string",
    fields_app_encryption_declarations=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_review_submissions=["betaReviewState"],
    fields_beta_build_localizations=["build"],
    fields_beta_testers=["apps"],
    fields_build_beta_details=["autoNotifyEnabled"],
    fields_build_icons=["iconAsset"],
    fields_builds=["app"],
    fields_diagnostic_signatures=["diagnosticType"],
    fields_perf_power_metrics=["deviceType"],
    fields_pre_release_versions=["app"],
    include=["app"],
    limit_beta_build_localizations=123,
    limit_beta_groups=123,
    limit_build_bundles=123,
    limit_icons=123,
    limit_individual_testers=123,
)
```

---

### 
> 

```python
client.v1.builds.app.list(id="string", fields_apps=["alternativeDistributionKey"])
```

---

### 
> 

```python
client.v1.builds.app_encryption_declaration.list(
    id="string", fields_app_encryption_declarations=["app"]
)
```

---

### 
> 

```python
client.v1.builds.app_store_version.list(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    fields_app_clip_default_experiences=["action"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_version_localizations=["appPreviewSets"],
    fields_app_store_version_phased_releases=["appStoreVersion"],
    fields_app_store_version_submissions=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    fields_routing_app_coverages=["appStoreVersion"],
    include=["ageRatingDeclaration"],
    limit_app_store_version_experiments_v2=123,
    limit_app_store_version_experiments=123,
    limit_app_store_version_localizations=123,
)
```

---

### 
> 

```python
client.v1.builds.beta_app_review_submission.list(
    id="string", fields_beta_app_review_submissions=["betaReviewState"]
)
```

---

### 
> 

```python
client.v1.builds.beta_build_localizations.list(
    id="string", fields_beta_build_localizations=["build"], limit=123
)
```

---

### 
> 

```python
client.v1.builds.build_beta_detail.list(
    id="string",
    fields_build_beta_details=["autoNotifyEnabled"],
    fields_builds=["app"],
    include=["build"],
)
```

---

### 
> 

```python
client.v1.builds.diagnostic_signatures.list(
    id="string",
    fields_diagnostic_signatures=["diagnosticType"],
    filter_diagnostic_type=["DISK_WRITES"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.builds.icons.list(id="string", fields_build_icons=["iconAsset"], limit=123)
```

---

### 
> 

```python
client.v1.builds.individual_testers.list(
    id="string", fields_beta_testers=["apps"], limit=123
)
```

---

### 
> 

```python
client.v1.builds.metrics.beta_build_usages.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.builds.perf_power_metrics.list(
    id="string",
    filter_device_type=["string"],
    filter_metric_type=["DISK"],
    filter_platform=["IOS"],
)
```

---

### 
> 

```python
client.v1.builds.pre_release_version.list(
    id="string", fields_pre_release_versions=["app"]
)
```

---

### 
> 

```python
client.v1.builds.relationships.app_encryption_declaration.list(id="string")
```

---

### 
> 

```python
client.v1.builds.relationships.individual_testers.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.bundle_ids.list(
    fields_apps=["alternativeDistributionKey"],
    fields_bundle_id_capabilities=["bundleId"],
    fields_bundle_ids=["app"],
    fields_profiles=["bundleId"],
    filter_id=["string"],
    filter_identifier=["string"],
    filter_name=["string"],
    filter_platform=["IOS"],
    filter_seed_id=["string"],
    include=["app"],
    limit=123,
    limit_bundle_id_capabilities=123,
    limit_profiles=123,
    sort=["id"],
)
```

---

### 
> 

```python
client.v1.bundle_ids.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_bundle_id_capabilities=["bundleId"],
    fields_bundle_ids=["app"],
    fields_profiles=["bundleId"],
    include=["app"],
    limit_bundle_id_capabilities=123,
    limit_profiles=123,
)
```

---

### 
> 

```python
client.v1.bundle_ids.app.list(id="string", fields_apps=["alternativeDistributionKey"])
```

---

### 
> 

```python
client.v1.bundle_ids.bundle_id_capabilities.list(
    id="string", fields_bundle_id_capabilities=["bundleId"], limit=123
)
```

---

### 
> 

```python
client.v1.bundle_ids.profiles.list(id="string", fields_profiles=["bundleId"], limit=123)
```

---

### 
> 

```python
client.v1.certificates.list(
    fields_certificates=["certificateContent"],
    filter_certificate_type=["IOS_DEVELOPMENT"],
    filter_display_name=["string"],
    filter_id=["string"],
    filter_serial_number=["string"],
    limit=123,
    sort=["certificateType"],
)
```

---

### 
> 

```python
client.v1.certificates.get(id="string", fields_certificates=["certificateContent"])
```

---

### 
> 

```python
client.v1.ci_artifacts.get(id="string", fields_ci_artifacts=["downloadUrl"])
```

---

### 
> 

```python
client.v1.ci_build_actions.get(
    id="string",
    fields_ci_artifacts=["downloadUrl"],
    fields_ci_build_actions=["actionType"],
    fields_ci_build_runs=["actions"],
    fields_ci_issues=["category"],
    fields_ci_test_results=["className"],
    include=["buildRun"],
)
```

---

### 
> 

```python
client.v1.ci_build_actions.artifacts.list(
    id="string", fields_ci_artifacts=["downloadUrl"], limit=123
)
```

---

### 
> 

```python
client.v1.ci_build_actions.build_run.list(
    id="string",
    fields_builds=["app"],
    fields_ci_build_runs=["actions"],
    fields_ci_products=["additionalRepositories"],
    fields_ci_workflows=["actions"],
    fields_scm_git_references=["canonicalName"],
    fields_scm_pull_requests=["destinationBranchName"],
    include=["builds"],
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.ci_build_actions.issues.list(
    id="string", fields_ci_issues=["category"], limit=123
)
```

---

### 
> 

```python
client.v1.ci_build_actions.test_results.list(
    id="string", fields_ci_test_results=["className"], limit=123
)
```

---

### 
> 

```python
client.v1.ci_build_runs.get(
    id="string",
    fields_builds=["app"],
    fields_ci_build_actions=["actionType"],
    fields_ci_build_runs=["actions"],
    include=["builds"],
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.ci_build_runs.actions.list(
    id="string",
    fields_ci_build_actions=["actionType"],
    fields_ci_build_runs=["actions"],
    include=["buildRun"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.ci_build_runs.builds.list(
    id="string",
    fields_app_encryption_declarations=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_review_submissions=["betaReviewState"],
    fields_beta_build_localizations=["build"],
    fields_beta_groups=["app"],
    fields_beta_testers=["apps"],
    fields_build_beta_details=["autoNotifyEnabled"],
    fields_build_bundles=["appClipDomainCacheStatus"],
    fields_build_icons=["iconAsset"],
    fields_builds=["app"],
    fields_pre_release_versions=["app"],
    filter_app_store_version=["string"],
    filter_app=["string"],
    filter_beta_app_review_submission_beta_review_state=["WAITING_FOR_REVIEW"],
    filter_beta_groups=["string"],
    filter_build_audience_type=["INTERNAL_ONLY"],
    filter_expired=["string"],
    filter_id=["string"],
    filter_pre_release_version_platform=["IOS"],
    filter_pre_release_version_version=["string"],
    filter_pre_release_version=["string"],
    filter_processing_state=["PROCESSING"],
    filter_uses_non_exempt_encryption=["string"],
    filter_version=["string"],
    include=["app"],
    limit=123,
    limit_beta_build_localizations=123,
    limit_beta_groups=123,
    limit_build_bundles=123,
    limit_icons=123,
    limit_individual_testers=123,
    sort=["preReleaseVersion"],
)
```

---

### 
> 

```python
client.v1.ci_issues.get(id="string", fields_ci_issues=["category"])
```

---

### 
> 

```python
client.v1.ci_mac_os_versions.list(
    fields_ci_mac_os_versions=["name"],
    fields_ci_xcode_versions=["macOsVersions"],
    include=["xcodeVersions"],
    limit=123,
    limit_xcode_versions=123,
)
```

---

### 
> 

```python
client.v1.ci_mac_os_versions.get(
    id="string",
    fields_ci_mac_os_versions=["name"],
    fields_ci_xcode_versions=["macOsVersions"],
    include=["xcodeVersions"],
    limit_xcode_versions=123,
)
```

---

### 
> 

```python
client.v1.ci_mac_os_versions.xcode_versions.list(
    id="string",
    fields_ci_mac_os_versions=["name"],
    fields_ci_xcode_versions=["macOsVersions"],
    include=["macOsVersions"],
    limit=123,
    limit_mac_os_versions=123,
)
```

---

### 
> 

```python
client.v1.ci_products.list(
    fields_apps=["alternativeDistributionKey"],
    fields_ci_build_runs=["actions"],
    fields_ci_products=["additionalRepositories"],
    fields_ci_workflows=["actions"],
    fields_scm_repositories=["defaultBranch"],
    filter_app=["string"],
    filter_product_type=["APP"],
    include=["app"],
    limit=123,
    limit_primary_repositories=123,
)
```

---

### 
> 

```python
client.v1.ci_products.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_ci_build_runs=["actions"],
    fields_ci_products=["additionalRepositories"],
    fields_ci_workflows=["actions"],
    fields_scm_repositories=["defaultBranch"],
    include=["app"],
    limit_primary_repositories=123,
)
```

---

### 
> 

```python
client.v1.ci_products.additional_repositories.list(
    id="string",
    fields_scm_git_references=["canonicalName"],
    fields_scm_providers=["repositories"],
    fields_scm_repositories=["defaultBranch"],
    filter_id=["string"],
    include=["defaultBranch"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.ci_products.app.list(
    id="string",
    fields_app_clips=["app"],
    fields_app_custom_product_pages=["app"],
    fields_app_encryption_declarations=["app"],
    fields_app_events=["app"],
    fields_app_infos=["ageRatingDeclaration"],
    fields_app_pre_orders=["app"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_beta_app_localizations=["app"],
    fields_beta_app_review_details=["app"],
    fields_beta_groups=["app"],
    fields_beta_license_agreements=["agreementText"],
    fields_builds=["app"],
    fields_ci_products=["additionalRepositories"],
    fields_end_user_license_agreements=["agreementText"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_enabled_versions=["app"],
    fields_in_app_purchases=["app"],
    fields_pre_release_versions=["app"],
    fields_promoted_purchases=["app"],
    fields_review_submissions=["app"],
    fields_subscription_grace_periods=["duration"],
    fields_subscription_groups=["app"],
    include=["appClips"],
    limit_app_clips=123,
    limit_app_custom_product_pages=123,
    limit_app_encryption_declarations=123,
    limit_app_events=123,
    limit_app_infos=123,
    limit_app_store_version_experiments_v2=123,
    limit_app_store_versions=123,
    limit_beta_app_localizations=123,
    limit_beta_groups=123,
    limit_builds=123,
    limit_game_center_enabled_versions=123,
    limit_in_app_purchases_v2=123,
    limit_in_app_purchases=123,
    limit_pre_release_versions=123,
    limit_promoted_purchases=123,
    limit_review_submissions=123,
    limit_subscription_groups=123,
)
```

---

### 
> 

```python
client.v1.ci_products.build_runs.list(
    id="string",
    fields_builds=["app"],
    fields_ci_build_runs=["actions"],
    fields_ci_products=["additionalRepositories"],
    fields_ci_workflows=["actions"],
    fields_scm_git_references=["canonicalName"],
    fields_scm_pull_requests=["destinationBranchName"],
    filter_builds=["string"],
    include=["builds"],
    limit=123,
    limit_builds=123,
    sort=["number"],
)
```

---

### 
> 

```python
client.v1.ci_products.primary_repositories.list(
    id="string",
    fields_scm_git_references=["canonicalName"],
    fields_scm_providers=["repositories"],
    fields_scm_repositories=["defaultBranch"],
    filter_id=["string"],
    include=["defaultBranch"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.ci_products.workflows.list(
    id="string",
    fields_ci_mac_os_versions=["name"],
    fields_ci_products=["additionalRepositories"],
    fields_ci_workflows=["actions"],
    fields_ci_xcode_versions=["macOsVersions"],
    fields_scm_repositories=["defaultBranch"],
    include=["macOsVersion"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.ci_test_results.get(id="string", fields_ci_test_results=["className"])
```

---

### 
> 

```python
client.v1.ci_workflows.get(
    id="string",
    fields_ci_build_runs=["actions"],
    fields_ci_workflows=["actions"],
    fields_scm_repositories=["defaultBranch"],
    include=["macOsVersion"],
)
```

---

### 
> 

```python
client.v1.ci_workflows.build_runs.list(
    id="string",
    fields_builds=["app"],
    fields_ci_build_runs=["actions"],
    fields_ci_products=["additionalRepositories"],
    fields_ci_workflows=["actions"],
    fields_scm_git_references=["canonicalName"],
    fields_scm_pull_requests=["destinationBranchName"],
    filter_builds=["string"],
    include=["builds"],
    limit=123,
    limit_builds=123,
    sort=["number"],
)
```

---

### 
> 

```python
client.v1.ci_workflows.repository.list(
    id="string",
    fields_scm_git_references=["canonicalName"],
    fields_scm_providers=["repositories"],
    fields_scm_repositories=["defaultBranch"],
    include=["defaultBranch"],
)
```

---

### 
> 

```python
client.v1.ci_xcode_versions.list(
    fields_ci_mac_os_versions=["name"],
    fields_ci_xcode_versions=["macOsVersions"],
    include=["macOsVersions"],
    limit=123,
    limit_mac_os_versions=123,
)
```

---

### 
> 

```python
client.v1.ci_xcode_versions.get(
    id="string",
    fields_ci_mac_os_versions=["name"],
    fields_ci_xcode_versions=["macOsVersions"],
    include=["macOsVersions"],
    limit_mac_os_versions=123,
)
```

---

### 
> 

```python
client.v1.ci_xcode_versions.mac_os_versions.list(
    id="string",
    fields_ci_mac_os_versions=["name"],
    fields_ci_xcode_versions=["macOsVersions"],
    include=["xcodeVersions"],
    limit=123,
    limit_xcode_versions=123,
)
```

---

### 
> 

```python
client.v1.customer_review_responses.get(
    id="string",
    fields_customer_review_responses=["lastModifiedDate"],
    include=["review"],
)
```

---

### 
> 

```python
client.v1.customer_reviews.get(
    id="string",
    fields_customer_review_responses=["lastModifiedDate"],
    fields_customer_reviews=["body"],
    include=["response"],
)
```

---

### 
> 

```python
client.v1.customer_reviews.response.list(
    id="string",
    fields_customer_review_responses=["lastModifiedDate"],
    fields_customer_reviews=["body"],
    include=["review"],
)
```

---

### 
> 

```python
client.v1.devices.list(
    fields_devices=["addedDate"],
    filter_id=["string"],
    filter_name=["string"],
    filter_platform=["IOS"],
    filter_status=["ENABLED"],
    filter_udid=["string"],
    limit=123,
    sort=["id"],
)
```

---

### 
> 

```python
client.v1.devices.get(id="string", fields_devices=["addedDate"])
```

---

### 
> 

```python
client.v1.diagnostic_signatures.logs.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.end_user_license_agreements.get(
    id="string",
    fields_end_user_license_agreements=["agreementText"],
    fields_territories=["currency"],
    include=["app"],
    limit_territories=123,
)
```

---

### 
> 

```python
client.v1.end_user_license_agreements.territories.list(
    id="string", fields_territories=["currency"], limit=123
)
```

---

### 
> 

```python
client.v1.finance_reports.list(
    filter_region_code=["string"],
    filter_report_date=["string"],
    filter_report_type=["FINANCIAL"],
    filter_vendor_number=["string"],
)
```

---

### 
> 

```python
client.v1.game_center_achievement_images.get(
    id="string",
    fields_game_center_achievement_images=["assetDeliveryState"],
    include=["gameCenterAchievementLocalization"],
)
```

---

### 
> 

```python
client.v1.game_center_achievement_localizations.get(
    id="string",
    fields_game_center_achievement_images=["assetDeliveryState"],
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievements=["archived"],
    include=["gameCenterAchievement"],
)
```

---

### 
> 

```python
client.v1.game_center_achievement_localizations.game_center_achievement.list(
    id="string",
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    include=["gameCenterDetail"],
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_achievement_localizations.game_center_achievement_image.list(
    id="string",
    fields_game_center_achievement_images=["assetDeliveryState"],
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    include=["gameCenterAchievementLocalization"],
)
```

---

### 
> 

```python
client.v1.game_center_achievement_releases.get(
    id="string",
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    include=["gameCenterAchievement"],
)
```

---

### 
> 

```python
client.v1.game_center_achievements.get(
    id="string",
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    include=["gameCenterDetail"],
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_achievements.group_achievement.list(
    id="string",
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    include=["gameCenterDetail"],
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_achievements.localizations.list(
    id="string",
    fields_game_center_achievement_images=["assetDeliveryState"],
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievements=["archived"],
    include=["gameCenterAchievement"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_achievements.relationships.group_achievement.list(id="string")
```

---

### 
> 

```python
client.v1.game_center_achievements.releases.list(
    id="string",
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    filter_game_center_detail=["string"],
    filter_live=["string"],
    include=["gameCenterAchievement"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.get(
    id="string",
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_game_center_app_versions=["appStoreVersion"],
    include=["appStoreVersion"],
    limit_compatibility_versions=123,
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.app_store_version.list(
    id="string",
    fields_age_rating_declarations=["ageRatingOverride"],
    fields_alternative_distribution_packages=["appStoreVersion"],
    fields_app_clip_default_experiences=["action"],
    fields_app_store_review_details=["appStoreReviewAttachments"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_version_localizations=["appPreviewSets"],
    fields_app_store_version_phased_releases=["appStoreVersion"],
    fields_app_store_version_submissions=["appStoreVersion"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    fields_routing_app_coverages=["appStoreVersion"],
    include=["ageRatingDeclaration"],
    limit_app_store_version_experiments_v2=123,
    limit_app_store_version_experiments=123,
    limit_app_store_version_localizations=123,
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.compatibility_versions.list(
    id="string",
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_game_center_app_versions=["appStoreVersion"],
    filter_enabled=["string"],
    include=["appStoreVersion"],
    limit=123,
    limit_compatibility_versions=123,
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.relationships.compatibility_versions.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_details.get(
    id="string",
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_app_versions=["appStoreVersion"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["achievementReleases"],
    limit_achievement_releases=123,
    limit_game_center_achievements=123,
    limit_game_center_app_versions=123,
    limit_game_center_leaderboard_sets=123,
    limit_game_center_leaderboards=123,
    limit_leaderboard_releases=123,
    limit_leaderboard_set_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.achievement_releases.list(
    id="string",
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    filter_game_center_achievement=["string"],
    filter_live=["string"],
    include=["gameCenterAchievement"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.game_center_achievements.list(
    id="string",
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    filter_archived=["string"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.game_center_app_versions.list(
    id="string",
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_game_center_app_versions=["appStoreVersion"],
    filter_enabled=["string"],
    include=["appStoreVersion"],
    limit=123,
    limit_compatibility_versions=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.game_center_group.list(
    id="string",
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterAchievements"],
    limit_game_center_achievements=123,
    limit_game_center_details=123,
    limit_game_center_leaderboard_sets=123,
    limit_game_center_leaderboards=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.game_center_leaderboard_sets.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_game_center_leaderboards=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.game_center_leaderboards.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_archived=["string"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_game_center_leaderboard_sets=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.leaderboard_releases.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_game_center_leaderboard=["string"],
    filter_live=["string"],
    include=["gameCenterDetail"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.leaderboard_set_releases.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    filter_game_center_leaderboard_set=["string"],
    filter_live=["string"],
    include=["gameCenterDetail"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_details.metrics.classic_matchmaking_requests.list(
    id="string",
    granularity="P1D",
    filter_result="MATCHED",
    group_by=["result"],
    limit=123,
    sort=["averageSecondsInQueue"],
)
```

---

### 
> 

```python
client.v1.game_center_details.metrics.rule_based_matchmaking_requests.list(
    id="string",
    granularity="P1D",
    filter_result="MATCHED",
    group_by=["result"],
    limit=123,
    sort=["averageSecondsInQueue"],
)
```

---

### 
> 

```python
client.v1.game_center_details.relationships.game_center_achievements.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_details.relationships.game_center_leaderboard_sets.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_details.relationships.game_center_leaderboards.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_enabled_versions.compatible_versions.list(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_game_center_enabled_versions=["app"],
    filter_app=["string"],
    filter_id=["string"],
    filter_platform=["IOS"],
    filter_version_string=["string"],
    include=["app"],
    limit=123,
    limit_compatible_versions=123,
    sort=["versionString"],
)
```

---

### 
> 

```python
client.v1.game_center_enabled_versions.relationships.compatible_versions.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_groups.list(
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_game_center_details=["string"],
    include=["gameCenterAchievements"],
    limit=123,
    limit_game_center_achievements=123,
    limit_game_center_details=123,
    limit_game_center_leaderboard_sets=123,
    limit_game_center_leaderboards=123,
)
```

---

### 
> 

```python
client.v1.game_center_groups.get(
    id="string",
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterAchievements"],
    limit_game_center_achievements=123,
    limit_game_center_details=123,
    limit_game_center_leaderboard_sets=123,
    limit_game_center_leaderboards=123,
)
```

---

### 
> 

```python
client.v1.game_center_groups.game_center_achievements.list(
    id="string",
    fields_game_center_achievement_localizations=["afterEarnedDescription"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    filter_archived=["string"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_groups.game_center_details.list(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_game_center_achievement_releases=["gameCenterAchievement"],
    fields_game_center_achievements=["archived"],
    fields_game_center_app_versions=["appStoreVersion"],
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_game_center_app_versions_enabled=["string"],
    include=["achievementReleases"],
    limit=123,
    limit_achievement_releases=123,
    limit_game_center_achievements=123,
    limit_game_center_app_versions=123,
    limit_game_center_leaderboard_sets=123,
    limit_game_center_leaderboards=123,
    limit_leaderboard_releases=123,
    limit_leaderboard_set_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_groups.game_center_leaderboard_sets.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_game_center_leaderboards=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_groups.game_center_leaderboards.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_archived=["string"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_game_center_leaderboard_sets=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_groups.relationships.game_center_achievements.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_groups.relationships.game_center_leaderboard_sets.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_groups.relationships.game_center_leaderboards.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_images.get(
    id="string",
    fields_game_center_leaderboard_images=["assetDeliveryState"],
    include=["gameCenterLeaderboardLocalization"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_localizations.get(
    id="string",
    fields_game_center_leaderboard_images=["assetDeliveryState"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    include=["gameCenterLeaderboard"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_localizations.game_center_leaderboard_image.list(
    id="string",
    fields_game_center_leaderboard_images=["assetDeliveryState"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    include=["gameCenterLeaderboardLocalization"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_releases.get(
    id="string",
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    include=["gameCenterDetail"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_images.get(
    id="string",
    fields_game_center_leaderboard_set_images=["assetDeliveryState"],
    include=["gameCenterLeaderboardSetLocalization"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_localizations.get(
    id="string",
    fields_game_center_leaderboard_set_images=["assetDeliveryState"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    include=["gameCenterLeaderboardSet"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_localizations.game_center_leaderboard_set_image.list(
    id="string",
    fields_game_center_leaderboard_set_images=["assetDeliveryState"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    include=["gameCenterLeaderboardSetLocalization"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_member_localizations.list(
    filter_game_center_leaderboard_set=["string"],
    filter_game_center_leaderboard=["string"],
    fields_game_center_leaderboard_set_member_localizations=["gameCenterLeaderboard"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterLeaderboard"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_member_localizations.game_center_leaderboard.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterDetail"],
    limit_game_center_leaderboard_sets=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_member_localizations.game_center_leaderboard_set.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterDetail"],
    limit_game_center_leaderboards=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_releases.get(
    id="string",
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    include=["gameCenterDetail"],
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.get(
    id="string",
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterDetail"],
    limit_game_center_leaderboards=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.game_center_leaderboards.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_archived=["string"],
    filter_id=["string"],
    filter_reference_name=["string"],
    include=["gameCenterDetail"],
    limit=123,
    limit_game_center_leaderboard_sets=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.group_leaderboard_set.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterDetail"],
    limit_game_center_leaderboards=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.localizations.list(
    id="string",
    fields_game_center_leaderboard_set_images=["assetDeliveryState"],
    fields_game_center_leaderboard_set_localizations=["gameCenterLeaderboardSet"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    include=["gameCenterLeaderboardSet"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.relationships.game_center_leaderboards.list(
    id="string", limit=123
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.relationships.group_leaderboard_set.list(
    id="string"
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.releases.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_leaderboard_set_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    filter_game_center_detail=["string"],
    filter_live=["string"],
    include=["gameCenterDetail"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.get(
    id="string",
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterDetail"],
    limit_game_center_leaderboard_sets=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.group_leaderboard.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_groups=["gameCenterAchievements"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboard_sets=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterDetail"],
    limit_game_center_leaderboard_sets=123,
    limit_localizations=123,
    limit_releases=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.localizations.list(
    id="string",
    fields_game_center_leaderboard_images=["assetDeliveryState"],
    fields_game_center_leaderboard_localizations=["formatterOverride"],
    fields_game_center_leaderboards=["archived"],
    include=["gameCenterLeaderboard"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.relationships.group_leaderboard.list(id="string")
```

---

### 
> 

```python
client.v1.game_center_leaderboards.releases.list(
    id="string",
    fields_game_center_details=["achievementReleases"],
    fields_game_center_leaderboard_releases=["gameCenterDetail"],
    fields_game_center_leaderboards=["archived"],
    filter_game_center_detail=["string"],
    filter_live=["string"],
    include=["gameCenterDetail"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.list(
    fields_game_center_matchmaking_queues=["classicMatchmakingBundleIds"],
    include=["experimentRuleSet"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.get(
    id="string",
    fields_game_center_matchmaking_queues=["classicMatchmakingBundleIds"],
    include=["experimentRuleSet"],
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.metrics.experiment_matchmaking_queue_sizes.list(
    id="string", granularity="P1D", limit=123, sort=["averageNumberOfRequests"]
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.metrics.experiment_matchmaking_requests.list(
    id="string",
    granularity="P1D",
    filter_game_center_detail="string",
    filter_result="MATCHED",
    group_by=["gameCenterDetail"],
    limit=123,
    sort=["averageSecondsInQueue"],
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.metrics.matchmaking_queue_sizes.list(
    id="string", granularity="P1D", limit=123, sort=["averageNumberOfRequests"]
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.metrics.matchmaking_requests.list(
    id="string",
    granularity="P1D",
    filter_game_center_detail="string",
    filter_result="MATCHED",
    group_by=["gameCenterDetail"],
    limit=123,
    sort=["averageSecondsInQueue"],
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.metrics.matchmaking_sessions.list(
    id="string", granularity="P1D", limit=123, sort=["averagePlayerCount"]
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.list(
    fields_game_center_matchmaking_queues=["classicMatchmakingBundleIds"],
    fields_game_center_matchmaking_rule_sets=["matchmakingQueues"],
    fields_game_center_matchmaking_rules=["description"],
    fields_game_center_matchmaking_teams=["maxPlayers"],
    include=["matchmakingQueues"],
    limit=123,
    limit_matchmaking_queues=123,
    limit_rules=123,
    limit_teams=123,
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.get(
    id="string",
    fields_game_center_matchmaking_queues=["classicMatchmakingBundleIds"],
    fields_game_center_matchmaking_rule_sets=["matchmakingQueues"],
    fields_game_center_matchmaking_rules=["description"],
    fields_game_center_matchmaking_teams=["maxPlayers"],
    include=["matchmakingQueues"],
    limit_matchmaking_queues=123,
    limit_rules=123,
    limit_teams=123,
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.matchmaking_queues.list(
    id="string",
    fields_game_center_matchmaking_queues=["classicMatchmakingBundleIds"],
    fields_game_center_matchmaking_rule_sets=["matchmakingQueues"],
    include=["experimentRuleSet"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.rules.list(
    id="string", fields_game_center_matchmaking_rules=["description"], limit=123
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.teams.list(
    id="string", fields_game_center_matchmaking_teams=["maxPlayers"], limit=123
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rules.metrics.matchmaking_boolean_rule_results.list(
    id="string",
    granularity="P1D",
    filter_game_center_matchmaking_queue="string",
    filter_result="string",
    group_by=["gameCenterMatchmakingQueue"],
    limit=123,
    sort=["count"],
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rules.metrics.matchmaking_number_rule_results.list(
    id="string",
    granularity="P1D",
    filter_game_center_matchmaking_queue="string",
    group_by=["gameCenterMatchmakingQueue"],
    limit=123,
    sort=["averageResult"],
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rules.metrics.matchmaking_rule_errors.list(
    id="string",
    granularity="P1D",
    filter_game_center_matchmaking_queue="string",
    group_by=["gameCenterMatchmakingQueue"],
    limit=123,
    sort=["count"],
)
```

---

### 
> 

```python
client.v1.in_app_purchase_app_store_review_screenshots.get(
    id="string",
    fields_in_app_purchase_app_store_review_screenshots=["assetDeliveryState"],
    include=["inAppPurchaseV2"],
)
```

---

### 
> 

```python
client.v1.in_app_purchase_availabilities.get(
    id="string",
    fields_in_app_purchase_availabilities=["availableInNewTerritories"],
    fields_territories=["currency"],
    include=["availableTerritories"],
    limit_available_territories=123,
)
```

---

### 
> 

```python
client.v1.in_app_purchase_availabilities.available_territories.list(
    id="string", fields_territories=["currency"], limit=123
)
```

---

### 
> 

```python
client.v1.in_app_purchase_contents.get(
    id="string",
    fields_in_app_purchase_contents=["fileName"],
    include=["inAppPurchaseV2"],
)
```

---

### 
> 

```python
client.v1.in_app_purchase_localizations.get(
    id="string",
    fields_in_app_purchase_localizations=["description"],
    include=["inAppPurchaseV2"],
)
```

---

### 
> 

```python
client.v1.in_app_purchase_price_schedules.get(
    id="string",
    fields_in_app_purchase_price_schedules=["automaticPrices"],
    fields_in_app_purchase_prices=["endDate"],
    fields_territories=["currency"],
    include=["automaticPrices"],
    limit_automatic_prices=123,
    limit_manual_prices=123,
)
```

---

### 
> 

```python
client.v1.in_app_purchase_price_schedules.automatic_prices.list(
    id="string",
    fields_in_app_purchase_price_points=["customerPrice"],
    fields_in_app_purchase_prices=["endDate"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["inAppPurchasePricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.in_app_purchase_price_schedules.base_territory.list(
    id="string", fields_territories=["currency"]
)
```

---

### 
> 

```python
client.v1.in_app_purchase_price_schedules.manual_prices.list(
    id="string",
    fields_in_app_purchase_price_points=["customerPrice"],
    fields_in_app_purchase_prices=["endDate"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["inAppPurchasePricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.in_app_purchases.get(
    id="string", fields_in_app_purchases=["apps"], include=["apps"], limit_apps=123
)
```

---

### 
> 

```python
client.v1.marketplace_domains.list(
    fields_marketplace_domains=["createdDate"], limit=123
)
```

---

### 
> 

```python
client.v1.marketplace_domains.get(
    id="string", fields_marketplace_domains=["createdDate"]
)
```

---

### 
> 

```python
client.v1.marketplace_webhooks.list(
    fields_marketplace_webhooks=["endpointUrl"], limit=123
)
```

---

### 
> 

```python
client.v1.pre_release_versions.list(
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    fields_pre_release_versions=["app"],
    filter_app=["string"],
    filter_builds_expired=["string"],
    filter_builds_processing_state=["PROCESSING"],
    filter_builds_version=["string"],
    filter_builds=["string"],
    filter_platform=["IOS"],
    filter_version=["string"],
    include=["app"],
    limit=123,
    limit_builds=123,
    sort=["version"],
)
```

---

### 
> 

```python
client.v1.pre_release_versions.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_builds=["app"],
    fields_pre_release_versions=["app"],
    include=["app"],
    limit_builds=123,
)
```

---

### 
> 

```python
client.v1.pre_release_versions.app.list(
    id="string", fields_apps=["alternativeDistributionKey"]
)
```

---

### 
> 

```python
client.v1.pre_release_versions.builds.list(
    id="string", fields_builds=["app"], limit=123
)
```

---

### 
> 

```python
client.v1.profiles.list(
    fields_bundle_ids=["app"],
    fields_certificates=["certificateContent"],
    fields_devices=["addedDate"],
    fields_profiles=["bundleId"],
    filter_id=["string"],
    filter_name=["string"],
    filter_profile_state=["ACTIVE"],
    filter_profile_type=["IOS_APP_DEVELOPMENT"],
    include=["bundleId"],
    limit=123,
    limit_certificates=123,
    limit_devices=123,
    sort=["id"],
)
```

---

### 
> 

```python
client.v1.profiles.get(
    id="string",
    fields_bundle_ids=["app"],
    fields_certificates=["certificateContent"],
    fields_devices=["addedDate"],
    fields_profiles=["bundleId"],
    include=["bundleId"],
    limit_certificates=123,
    limit_devices=123,
)
```

---

### 
> 

```python
client.v1.profiles.bundle_id.list(id="string", fields_bundle_ids=["app"])
```

---

### 
> 

```python
client.v1.profiles.certificates.list(
    id="string", fields_certificates=["certificateContent"], limit=123
)
```

---

### 
> 

```python
client.v1.profiles.devices.list(id="string", fields_devices=["addedDate"], limit=123)
```

---

### 
> 

```python
client.v1.promoted_purchase_images.get(
    id="string",
    fields_promoted_purchase_images=["assetToken"],
    include=["promotedPurchase"],
)
```

---

### 
> 

```python
client.v1.promoted_purchases.get(
    id="string",
    fields_promoted_purchase_images=["assetToken"],
    fields_promoted_purchases=["app"],
    include=["inAppPurchaseV2"],
    limit_promotion_images=123,
)
```

---

### 
> 

```python
client.v1.promoted_purchases.promotion_images.list(
    id="string",
    fields_promoted_purchase_images=["assetToken"],
    fields_promoted_purchases=["app"],
    include=["promotedPurchase"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.review_submissions.list(
    filter_app=["string"],
    fields_review_submission_items=["appCustomProductPageVersion"],
    fields_review_submissions=["app"],
    filter_platform=["IOS"],
    filter_state=["READY_FOR_REVIEW"],
    include=["app"],
    limit=123,
    limit_items=123,
)
```

---

### 
> 

```python
client.v1.review_submissions.get(
    id="string",
    fields_review_submission_items=["appCustomProductPageVersion"],
    fields_review_submissions=["app"],
    include=["app"],
    limit_items=123,
)
```

---

### 
> 

```python
client.v1.review_submissions.items.list(
    id="string",
    fields_app_custom_product_page_versions=["appCustomProductPage"],
    fields_app_events=["app"],
    fields_app_store_version_experiments=["app"],
    fields_app_store_versions=["ageRatingDeclaration"],
    fields_review_submission_items=["appCustomProductPageVersion"],
    include=["appCustomProductPageVersion"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.routing_app_coverages.get(
    id="string",
    fields_routing_app_coverages=["appStoreVersion"],
    include=["appStoreVersion"],
)
```

---

### 
> 

```python
client.v1.sales_reports.list(
    filter_frequency=["DAILY"],
    filter_report_sub_type=["SUMMARY"],
    filter_report_type=["SALES"],
    filter_vendor_number=["string"],
    filter_report_date=["string"],
    filter_version=["string"],
)
```

---

### 
> 

```python
client.v1.scm_git_references.get(
    id="string", fields_scm_git_references=["canonicalName"], include=["repository"]
)
```

---

### 
> 

```python
client.v1.scm_providers.list(
    fields_scm_providers=["repositories"],
    fields_scm_repositories=["defaultBranch"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.scm_providers.get(
    id="string",
    fields_scm_providers=["repositories"],
    fields_scm_repositories=["defaultBranch"],
)
```

---

### 
> 

```python
client.v1.scm_providers.repositories.list(
    id="string",
    fields_scm_git_references=["canonicalName"],
    fields_scm_providers=["repositories"],
    fields_scm_repositories=["defaultBranch"],
    filter_id=["string"],
    include=["defaultBranch"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.scm_pull_requests.get(
    id="string",
    fields_scm_pull_requests=["destinationBranchName"],
    include=["repository"],
)
```

---

### 
> 

```python
client.v1.scm_repositories.list(
    fields_scm_git_references=["canonicalName"],
    fields_scm_pull_requests=["destinationBranchName"],
    fields_scm_repositories=["defaultBranch"],
    filter_id=["string"],
    include=["defaultBranch"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.scm_repositories.get(
    id="string",
    fields_scm_git_references=["canonicalName"],
    fields_scm_pull_requests=["destinationBranchName"],
    fields_scm_repositories=["defaultBranch"],
    include=["defaultBranch"],
)
```

---

### 
> 

```python
client.v1.scm_repositories.git_references.list(
    id="string",
    fields_scm_git_references=["canonicalName"],
    fields_scm_repositories=["defaultBranch"],
    include=["repository"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.scm_repositories.pull_requests.list(
    id="string",
    fields_scm_pull_requests=["destinationBranchName"],
    fields_scm_repositories=["defaultBranch"],
    include=["repository"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscription_app_store_review_screenshots.get(
    id="string",
    fields_subscription_app_store_review_screenshots=["assetDeliveryState"],
    include=["subscription"],
)
```

---

### 
> 

```python
client.v1.subscription_availabilities.get(
    id="string",
    fields_subscription_availabilities=["availableInNewTerritories"],
    fields_territories=["currency"],
    include=["availableTerritories"],
    limit_available_territories=123,
)
```

---

### 
> 

```python
client.v1.subscription_availabilities.available_territories.list(
    id="string", fields_territories=["currency"], limit=123
)
```

---

### 
> 

```python
client.v1.subscription_grace_periods.get(
    id="string", fields_subscription_grace_periods=["duration"]
)
```

---

### 
> 

```python
client.v1.subscription_group_localizations.get(
    id="string",
    fields_subscription_group_localizations=["customAppName"],
    include=["subscriptionGroup"],
)
```

---

### 
> 

```python
client.v1.subscription_groups.get(
    id="string",
    fields_subscription_group_localizations=["customAppName"],
    fields_subscription_groups=["app"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["subscriptionGroupLocalizations"],
    limit_subscription_group_localizations=123,
    limit_subscriptions=123,
)
```

---

### 
> 

```python
client.v1.subscription_groups.subscription_group_localizations.list(
    id="string",
    fields_subscription_group_localizations=["customAppName"],
    fields_subscription_groups=["app"],
    include=["subscriptionGroup"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscription_groups.subscriptions.list(
    id="string",
    fields_promoted_purchases=["app"],
    fields_subscription_app_store_review_screenshots=["assetDeliveryState"],
    fields_subscription_availabilities=["availableInNewTerritories"],
    fields_subscription_groups=["app"],
    fields_subscription_introductory_offers=["duration"],
    fields_subscription_localizations=["description"],
    fields_subscription_offer_codes=["active"],
    fields_subscription_prices=["preserveCurrentPrice"],
    fields_subscription_promotional_offers=["duration"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    filter_name=["string"],
    filter_product_id=["string"],
    filter_state=["MISSING_METADATA"],
    include=["appStoreReviewScreenshot"],
    limit=123,
    limit_introductory_offers=123,
    limit_offer_codes=123,
    limit_prices=123,
    limit_promotional_offers=123,
    limit_subscription_localizations=123,
    sort=["name"],
)
```

---

### 
> 

```python
client.v1.subscription_localizations.get(
    id="string",
    fields_subscription_localizations=["description"],
    include=["subscription"],
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_custom_codes.get(
    id="string",
    fields_subscription_offer_code_custom_codes=["active"],
    include=["offerCode"],
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_one_time_use_codes.get(
    id="string",
    fields_subscription_offer_code_one_time_use_codes=["active"],
    include=["offerCode"],
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_one_time_use_codes.values.list(id="string")
```

---

### 
> 

```python
client.v1.subscription_offer_codes.get(
    id="string",
    fields_subscription_offer_code_custom_codes=["active"],
    fields_subscription_offer_code_one_time_use_codes=["active"],
    fields_subscription_offer_code_prices=["subscriptionPricePoint"],
    fields_subscription_offer_codes=["active"],
    include=["customCodes"],
    limit_custom_codes=123,
    limit_one_time_use_codes=123,
    limit_prices=123,
)
```

---

### 
> 

```python
client.v1.subscription_offer_codes.custom_codes.list(
    id="string",
    fields_subscription_offer_code_custom_codes=["active"],
    fields_subscription_offer_codes=["active"],
    include=["offerCode"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscription_offer_codes.one_time_use_codes.list(
    id="string",
    fields_subscription_offer_code_one_time_use_codes=["active"],
    fields_subscription_offer_codes=["active"],
    include=["offerCode"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscription_offer_codes.prices.list(
    id="string",
    fields_subscription_offer_code_prices=["subscriptionPricePoint"],
    fields_subscription_price_points=["customerPrice"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["subscriptionPricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscription_price_points.get(
    id="string",
    fields_subscription_price_points=["customerPrice"],
    include=["territory"],
)
```

---

### 
> 

```python
client.v1.subscription_price_points.equalizations.list(
    id="string",
    fields_subscription_price_points=["customerPrice"],
    fields_territories=["currency"],
    filter_subscription=["string"],
    filter_territory=["string"],
    include=["territory"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscription_promotional_offers.get(
    id="string",
    fields_subscription_promotional_offer_prices=["subscriptionPricePoint"],
    fields_subscription_promotional_offers=["duration"],
    include=["prices"],
    limit_prices=123,
)
```

---

### 
> 

```python
client.v1.subscription_promotional_offers.prices.list(
    id="string",
    fields_subscription_price_points=["customerPrice"],
    fields_subscription_promotional_offer_prices=["subscriptionPricePoint"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["subscriptionPricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.get(
    id="string",
    fields_promoted_purchases=["app"],
    fields_subscription_app_store_review_screenshots=["assetDeliveryState"],
    fields_subscription_availabilities=["availableInNewTerritories"],
    fields_subscription_introductory_offers=["duration"],
    fields_subscription_localizations=["description"],
    fields_subscription_offer_codes=["active"],
    fields_subscription_price_points=["customerPrice"],
    fields_subscription_prices=["preserveCurrentPrice"],
    fields_subscription_promotional_offers=["duration"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["appStoreReviewScreenshot"],
    limit_introductory_offers=123,
    limit_offer_codes=123,
    limit_prices=123,
    limit_promotional_offers=123,
    limit_subscription_localizations=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.app_store_review_screenshot.list(
    id="string",
    fields_subscription_app_store_review_screenshots=["assetDeliveryState"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["subscription"],
)
```

---

### 
> 

```python
client.v1.subscriptions.introductory_offers.list(
    id="string",
    fields_subscription_introductory_offers=["duration"],
    fields_subscription_price_points=["customerPrice"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["subscription"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.offer_codes.list(
    id="string",
    fields_subscription_offer_code_custom_codes=["active"],
    fields_subscription_offer_code_one_time_use_codes=["active"],
    fields_subscription_offer_code_prices=["subscriptionPricePoint"],
    fields_subscription_offer_codes=["active"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    filter_territory=["string"],
    include=["customCodes"],
    limit=123,
    limit_custom_codes=123,
    limit_one_time_use_codes=123,
    limit_prices=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.price_points.list(
    id="string",
    fields_subscription_price_points=["customerPrice"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["territory"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.prices.list(
    id="string",
    fields_subscription_price_points=["customerPrice"],
    fields_subscription_prices=["preserveCurrentPrice"],
    fields_territories=["currency"],
    filter_subscription_price_point=["string"],
    filter_territory=["string"],
    include=["subscriptionPricePoint"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.promoted_purchase.list(
    id="string",
    fields_in_app_purchases=["app"],
    fields_promoted_purchase_images=["assetToken"],
    fields_promoted_purchases=["app"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["inAppPurchaseV2"],
    limit_promotion_images=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.promotional_offers.list(
    id="string",
    fields_subscription_promotional_offer_prices=["subscriptionPricePoint"],
    fields_subscription_promotional_offers=["duration"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    filter_territory=["string"],
    include=["prices"],
    limit=123,
    limit_prices=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.relationships.introductory_offers.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.subscriptions.relationships.prices.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.subscriptions.subscription_availability.list(
    id="string",
    fields_subscription_availabilities=["availableInNewTerritories"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    fields_territories=["currency"],
    include=["availableTerritories"],
    limit_available_territories=123,
)
```

---

### 
> 

```python
client.v1.subscriptions.subscription_localizations.list(
    id="string",
    fields_subscription_localizations=["description"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["subscription"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.territories.list(fields_territories=["currency"], limit=123)
```

---

### 
> 

```python
client.v1.user_invitations.list(
    fields_apps=["alternativeDistributionKey"],
    fields_user_invitations=["allAppsVisible"],
    filter_email=["string"],
    filter_roles=["ADMIN"],
    filter_visible_apps=["string"],
    include=["visibleApps"],
    limit=123,
    limit_visible_apps=123,
    sort=["email"],
)
```

---

### 
> 

```python
client.v1.user_invitations.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_user_invitations=["allAppsVisible"],
    include=["visibleApps"],
    limit_visible_apps=123,
)
```

---

### 
> 

```python
client.v1.user_invitations.visible_apps.list(
    id="string", fields_apps=["alternativeDistributionKey"], limit=123
)
```

---

### 
> 

```python
client.v1.users.list(
    fields_apps=["alternativeDistributionKey"],
    fields_users=["allAppsVisible"],
    filter_roles=["ADMIN"],
    filter_username=["string"],
    filter_visible_apps=["string"],
    include=["visibleApps"],
    limit=123,
    limit_visible_apps=123,
    sort=["lastName"],
)
```

---

### 
> 

```python
client.v1.users.get(
    id="string",
    fields_apps=["alternativeDistributionKey"],
    fields_users=["allAppsVisible"],
    include=["visibleApps"],
    limit_visible_apps=123,
)
```

---

### 
> 

```python
client.v1.users.relationships.visible_apps.list(id="string", limit=123)
```

---

### 
> 

```python
client.v1.users.visible_apps.list(
    id="string", fields_apps=["alternativeDistributionKey"], limit=123
)
```

---

### 
> 

```python
client.v2.app_availabilities.get(
    id="string",
    fields_app_availabilities=["app"],
    fields_territory_availabilities=["available"],
    include=["territoryAvailabilities"],
    limit_territory_availabilities=123,
)
```

---

### 
> 

```python
client.v2.app_availabilities.territory_availabilities.list(
    id="string",
    fields_territories=["currency"],
    fields_territory_availabilities=["available"],
    include=["territory"],
    limit=123,
)
```

---

### 
> 

```python
client.v2.app_store_version_experiments.get(
    id="string",
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["app"],
    include=["app"],
    limit_app_store_version_experiment_treatments=123,
    limit_control_versions=123,
)
```

---

### 
> 

```python
client.v2.app_store_version_experiments.app_store_version_experiment_treatments.list(
    id="string",
    fields_app_store_version_experiment_treatment_localizations=["appPreviewSets"],
    fields_app_store_version_experiment_treatments=["appIcon"],
    fields_app_store_version_experiments=["app"],
    include=["appStoreVersionExperiment"],
    limit=123,
    limit_app_store_version_experiment_treatment_localizations=123,
)
```

---

### 
> 

```python
client.v2.in_app_purchases.get(
    id="string",
    fields_in_app_purchase_app_store_review_screenshots=["assetDeliveryState"],
    fields_in_app_purchase_availabilities=["availableInNewTerritories"],
    fields_in_app_purchase_contents=["fileName"],
    fields_in_app_purchase_localizations=["description"],
    fields_in_app_purchase_price_points=["customerPrice"],
    fields_in_app_purchase_price_schedules=["automaticPrices"],
    fields_in_app_purchases=["app"],
    fields_promoted_purchases=["app"],
    include=["appStoreReviewScreenshot"],
    limit_in_app_purchase_localizations=123,
    limit_price_points=123,
)
```

---

### 
> 

```python
client.v2.in_app_purchases.app_store_review_screenshot.list(
    id="string",
    fields_in_app_purchase_app_store_review_screenshots=["assetDeliveryState"],
    fields_in_app_purchases=["app"],
    include=["inAppPurchaseV2"],
)
```

---

### 
> 

```python
client.v2.in_app_purchases.content.list(
    id="string",
    fields_in_app_purchase_contents=["fileName"],
    fields_in_app_purchases=["app"],
    include=["inAppPurchaseV2"],
)
```

---

### 
> 

```python
client.v2.in_app_purchases.iap_price_schedule.list(
    id="string",
    fields_in_app_purchase_price_schedules=["automaticPrices"],
    fields_in_app_purchase_prices=["endDate"],
    fields_in_app_purchases=["app"],
    fields_territories=["currency"],
    include=["automaticPrices"],
    limit_automatic_prices=123,
    limit_manual_prices=123,
)
```

---

### 
> 

```python
client.v2.in_app_purchases.in_app_purchase_availability.list(
    id="string",
    fields_in_app_purchase_availabilities=["availableInNewTerritories"],
    fields_territories=["currency"],
    include=["availableTerritories"],
    limit_available_territories=123,
)
```

---

### 
> 

```python
client.v2.in_app_purchases.in_app_purchase_localizations.list(
    id="string",
    fields_in_app_purchase_localizations=["description"],
    fields_in_app_purchases=["app"],
    include=["inAppPurchaseV2"],
    limit=123,
)
```

---

### 
> 

```python
client.v2.in_app_purchases.price_points.list(
    id="string",
    fields_in_app_purchase_price_points=["customerPrice"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["territory"],
    limit=123,
)
```

---

### 
> 

```python
client.v2.in_app_purchases.promoted_purchase.list(
    id="string",
    fields_in_app_purchases=["app"],
    fields_promoted_purchase_images=["assetToken"],
    fields_promoted_purchases=["app"],
    fields_subscriptions=["appStoreReviewScreenshot"],
    include=["inAppPurchaseV2"],
    limit_promotion_images=123,
)
```

---

### 
> 

```python
client.v2.sandbox_testers.list(fields_sandbox_testers=["acAccountName"], limit=123)
```

---

### 
> 

```python
client.v3.app_price_points.get(
    id="string", fields_app_price_points=["app"], include=["app"]
)
```

---

### 
> 

```python
client.v3.app_price_points.equalizations.list(
    id="string",
    fields_app_price_points=["app"],
    fields_apps=["alternativeDistributionKey"],
    fields_territories=["currency"],
    filter_territory=["string"],
    include=["app"],
    limit=123,
)
```

---

### 
> 

```python
client.v1.age_rating_declarations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "age_rating_override": "NONE",
                "alcohol_tobacco_or_drug_use_or_references": "NONE",
                "contests": "NONE",
                "gambling": True,
                "gambling_and_contests": True,
                "gambling_simulated": "NONE",
                "horror_or_fear_themes": "NONE",
                "kids_age_band": "FIVE_AND_UNDER",
                "mature_or_suggestive_themes": "NONE",
                "medical_or_treatment_information": "NONE",
                "profanity_or_crude_humor": "NONE",
                "seventeen_plus": True,
                "sexual_content_graphic_and_nudity": "NONE",
                "sexual_content_or_nudity": "NONE",
                "unrestricted_web_access": True,
                "violence_cartoon_or_fantasy": "NONE",
                "violence_realistic": "NONE",
                "violence_realistic_prolonged_graphic_or_sadistic": "NONE",
            },
            "id": "string",
            "type": "ageRatingDeclarations",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_clip_advanced_experience_images.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "appClipAdvancedExperienceImages",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_clip_advanced_experiences.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "action": "OPEN",
                "business_category": "AUTOMOTIVE",
                "default_language": "AR",
                "is_powered_by": True,
                "place": {
                    "categories": ["string"],
                    "display_point": {
                        "coordinates": {"latitude": 123.45, "longitude": 123.45},
                        "source": "CALCULATED",
                    },
                    "home_page": "string",
                    "main_address": {
                        "full_address": "string",
                        "structured_address": {
                            "country_code": "string",
                            "floor": "string",
                            "locality": "string",
                            "neighborhood": "string",
                            "postal_code": "string",
                            "state_province": "string",
                            "street_address": ["string"],
                        },
                    },
                    "map_action": "BUY_TICKETS",
                    "names": ["string"],
                    "phone_number": {
                        "intent": "string",
                        "number": "string",
                        "type": "FAX",
                    },
                    "place_id": "string",
                    "relationship": "OWNER",
                },
                "removed": True,
            },
            "id": "string",
            "relationships": {
                "app_clip": {"data": {"id": "string", "type": "appClips"}},
                "header_image": {
                    "data": {"id": "string", "type": "appClipAdvancedExperienceImages"}
                },
                "localizations": {
                    "data": [
                        {
                            "id": "string",
                            "type": "appClipAdvancedExperienceLocalizations",
                        }
                    ]
                },
            },
            "type": "appClipAdvancedExperiences",
        },
        "included": [
            {
                "attributes": {
                    "language": "AR",
                    "subtitle": "string",
                    "title": "string",
                },
                "id": "string",
                "type": "appClipAdvancedExperienceLocalizations",
            }
        ],
    },
)
```

---

### 
> 

```python
client.v1.app_clip_app_store_review_details.patch(
    id="string",
    data={
        "data": {
            "attributes": {"invocation_urls": ["http://www.example.com"]},
            "id": "string",
            "type": "appClipAppStoreReviewDetails",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_clip_default_experience_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"subtitle": "string"},
            "id": "string",
            "type": "appClipDefaultExperienceLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.patch(
    id="string",
    data={
        "data": {
            "attributes": {"action": "OPEN"},
            "id": "string",
            "relationships": {
                "release_with_app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appClipDefaultExperiences",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.relationships.release_with_app_store_version.patch(
    id="string", data={"data": {"id": "string", "type": "appStoreVersions"}}
)
```

---

### 
> 

```python
client.v1.app_clip_header_images.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "appClipHeaderImages",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"promotional_text": "string"},
            "id": "string",
            "type": "appCustomProductPageLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_versions.patch(
    id="string",
    data={
        "data": {
            "attributes": {"deep_link": "http://www.example.com"},
            "id": "string",
            "type": "appCustomProductPageVersions",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_custom_product_pages.patch(
    id="string",
    data={
        "data": {
            "attributes": {"name": "string", "visible": True},
            "id": "string",
            "type": "appCustomProductPages",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_encryption_declaration_documents.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "appEncryptionDeclarationDocuments",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_event_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "long_description": "string",
                "name": "string",
                "short_description": "string",
            },
            "id": "string",
            "type": "appEventLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_event_screenshots.patch(
    id="string",
    data={
        "data": {
            "attributes": {"uploaded": True},
            "id": "string",
            "type": "appEventScreenshots",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_event_video_clips.patch(
    id="string",
    data={
        "data": {
            "attributes": {"preview_frame_time_code": "string", "uploaded": True},
            "id": "string",
            "type": "appEventVideoClips",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_events.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "badge": "LIVE_EVENT",
                "deep_link": "http://www.example.com",
                "primary_locale": "string",
                "priority": "HIGH",
                "purchase_requirement": "NO_COST_ASSOCIATED",
                "purpose": "APPROPRIATE_FOR_ALL_USERS",
                "reference_name": "string",
                "territory_schedules": [
                    {
                        "event_end": "1970-01-01T00:00:00",
                        "event_start": "1970-01-01T00:00:00",
                        "publish_start": "1970-01-01T00:00:00",
                        "territories": ["string"],
                    }
                ],
            },
            "id": "string",
            "type": "appEvents",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_info_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "name": "string",
                "privacy_choices_url": "string",
                "privacy_policy_text": "string",
                "privacy_policy_url": "string",
                "subtitle": "string",
            },
            "id": "string",
            "type": "appInfoLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_infos.patch(
    id="string",
    data={
        "data": {
            "id": "string",
            "relationships": {
                "primary_category": {"data": {"id": "string", "type": "appCategories"}},
                "primary_subcategory_one": {
                    "data": {"id": "string", "type": "appCategories"}
                },
                "primary_subcategory_two": {
                    "data": {"id": "string", "type": "appCategories"}
                },
                "secondary_category": {
                    "data": {"id": "string", "type": "appCategories"}
                },
                "secondary_subcategory_one": {
                    "data": {"id": "string", "type": "appCategories"}
                },
                "secondary_subcategory_two": {
                    "data": {"id": "string", "type": "appCategories"}
                },
            },
            "type": "appInfos",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_pre_orders.patch(
    id="string",
    data={
        "data": {
            "attributes": {"app_release_date": "1970-01-01"},
            "id": "string",
            "type": "appPreOrders",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_preview_sets.relationships.app_previews.patch(
    id="string", data={"data": [{"id": "string", "type": "appPreviews"}]}
)
```

---

### 
> 

```python
client.v1.app_previews.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "preview_frame_time_code": "string",
                "source_file_checksum": "string",
                "uploaded": True,
            },
            "id": "string",
            "type": "appPreviews",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_screenshot_sets.relationships.app_screenshots.patch(
    id="string", data={"data": [{"id": "string", "type": "appScreenshots"}]}
)
```

---

### 
> 

```python
client.v1.app_screenshots.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "appScreenshots",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_review_attachments.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "appStoreReviewAttachments",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_review_details.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "contact_email": "string",
                "contact_first_name": "string",
                "contact_last_name": "string",
                "contact_phone": "string",
                "demo_account_name": "string",
                "demo_account_password": "string",
                "demo_account_required": True,
                "notes": "string",
            },
            "id": "string",
            "type": "appStoreReviewDetails",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatments.patch(
    id="string",
    data={
        "data": {
            "attributes": {"app_icon_name": "string", "name": "string"},
            "id": "string",
            "type": "appStoreVersionExperimentTreatments",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_version_experiments.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "name": "string",
                "started": True,
                "traffic_proportion": 123,
            },
            "id": "string",
            "type": "appStoreVersionExperiments",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_version_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "description": "string",
                "keywords": "string",
                "marketing_url": "http://www.example.com",
                "promotional_text": "string",
                "support_url": "http://www.example.com",
                "whats_new": "string",
            },
            "id": "string",
            "type": "appStoreVersionLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_version_phased_releases.patch(
    id="string",
    data={
        "data": {
            "attributes": {"phased_release_state": "INACTIVE"},
            "id": "string",
            "type": "appStoreVersionPhasedReleases",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_versions.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "copyright": "string",
                "downloadable": True,
                "earliest_release_date": "1970-01-01T00:00:00",
                "release_type": "MANUAL",
                "review_type": "APP_STORE",
                "version_string": "string",
            },
            "id": "string",
            "relationships": {
                "app_clip_default_experience": {
                    "data": {"id": "string", "type": "appClipDefaultExperiences"}
                },
                "build": {"data": {"id": "string", "type": "builds"}},
            },
            "type": "appStoreVersions",
        }
    },
)
```

---

### 
> 

```python
client.v1.app_store_versions.relationships.app_clip_default_experience.patch(
    id="string", data={"data": {"id": "string", "type": "appClipDefaultExperiences"}}
)
```

---

### 
> 

```python
client.v1.app_store_versions.relationships.build.patch(
    id="string", data={"data": {"id": "string", "type": "builds"}}
)
```

---

### 
> 

```python
client.v1.apps.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "bundle_id": "string",
                "content_rights_declaration": "DOES_NOT_USE_THIRD_PARTY_CONTENT",
                "primary_locale": "string",
                "subscription_status_url": "http://www.example.com",
                "subscription_status_url_for_sandbox": "http://www.example.com",
                "subscription_status_url_version": "V1",
                "subscription_status_url_version_for_sandbox": "V1",
            },
            "id": "string",
            "type": "apps",
        }
    },
)
```

---

### 
> 

```python
client.v1.apps.relationships.promoted_purchases.patch(
    id="string", data={"data": [{"id": "string", "type": "promotedPurchases"}]}
)
```

---

### 
> 

```python
client.v1.beta_app_clip_invocation_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"title": "string"},
            "id": "string",
            "type": "betaAppClipInvocationLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.beta_app_clip_invocations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"url": "http://www.example.com"},
            "id": "string",
            "type": "betaAppClipInvocations",
        }
    },
)
```

---

### 
> 

```python
client.v1.beta_app_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "description": "string",
                "feedback_email": "string",
                "marketing_url": "string",
                "privacy_policy_url": "string",
                "tv_os_privacy_policy": "string",
            },
            "id": "string",
            "type": "betaAppLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.beta_app_review_details.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "contact_email": "string",
                "contact_first_name": "string",
                "contact_last_name": "string",
                "contact_phone": "string",
                "demo_account_name": "string",
                "demo_account_password": "string",
                "demo_account_required": True,
                "notes": "string",
            },
            "id": "string",
            "type": "betaAppReviewDetails",
        }
    },
)
```

---

### 
> 

```python
client.v1.beta_build_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"whats_new": "string"},
            "id": "string",
            "type": "betaBuildLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.beta_groups.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "feedback_enabled": True,
                "ios_builds_available_for_apple_silicon_mac": True,
                "name": "string",
                "public_link_enabled": True,
                "public_link_limit": 123,
                "public_link_limit_enabled": True,
            },
            "id": "string",
            "type": "betaGroups",
        }
    },
)
```

---

### 
> 

```python
client.v1.beta_license_agreements.patch(
    id="string",
    data={
        "data": {
            "attributes": {"agreement_text": "string"},
            "id": "string",
            "type": "betaLicenseAgreements",
        }
    },
)
```

---

### 
> 

```python
client.v1.build_beta_details.patch(
    id="string",
    data={
        "data": {
            "attributes": {"auto_notify_enabled": True},
            "id": "string",
            "type": "buildBetaDetails",
        }
    },
)
```

---

### 
> 

```python
client.v1.builds.patch(
    id="string",
    data={
        "data": {
            "attributes": {"expired": True, "uses_non_exempt_encryption": True},
            "id": "string",
            "relationships": {
                "app_encryption_declaration": {
                    "data": {"id": "string", "type": "appEncryptionDeclarations"}
                }
            },
            "type": "builds",
        }
    },
)
```

---

### 
> 

```python
client.v1.builds.relationships.app_encryption_declaration.patch(
    id="string", data={"data": {"id": "string", "type": "appEncryptionDeclarations"}}
)
```

---

### 
> 

```python
client.v1.bundle_id_capabilities.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "capability_type": "ICLOUD",
                "settings": [
                    {
                        "allowed_instances": "ENTRY",
                        "description": "string",
                        "enabled_by_default": True,
                        "key": "ICLOUD_VERSION",
                        "min_instances": 123,
                        "name": "string",
                        "options": [
                            {
                                "description": "string",
                                "enabled": True,
                                "enabled_by_default": True,
                                "key": "XCODE_5",
                                "name": "string",
                                "supports_wildcard": True,
                            }
                        ],
                        "visible": True,
                    }
                ],
            },
            "id": "string",
            "type": "bundleIdCapabilities",
        }
    },
)
```

---

### 
> 

```python
client.v1.bundle_ids.patch(
    id="string",
    data={
        "data": {"attributes": {"name": "string"}, "id": "string", "type": "bundleIds"}
    },
)
```

---

### 
> 

```python
client.v1.ci_workflows.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "actions": [
                    {
                        "action_type": "BUILD",
                        "build_distribution_audience": "INTERNAL_ONLY",
                        "destination": "ANY_IOS_DEVICE",
                        "is_required_to_pass": True,
                        "name": "string",
                        "platform_field": "MACOS",
                        "scheme": "string",
                        "test_configuration": {
                            "kind": "USE_SCHEME_SETTINGS",
                            "test_destinations": [
                                {
                                    "device_type_identifier": "string",
                                    "device_type_name": "string",
                                    "kind": "SIMULATOR",
                                    "runtime_identifier": "string",
                                    "runtime_name": "string",
                                }
                            ],
                            "test_plan_name": "string",
                        },
                    }
                ],
                "branch_start_condition": {
                    "auto_cancel": True,
                    "files_and_folders_rule": {
                        "matchers": [
                            {
                                "directory": "string",
                                "file_extension": "string",
                                "file_name": "string",
                            }
                        ],
                        "mode": "START_IF_ANY_FILE_MATCHES",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "clean": True,
                "container_file_path": "string",
                "description": "string",
                "is_enabled": True,
                "is_locked_for_editing": True,
                "manual_branch_start_condition": {
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    }
                },
                "manual_pull_request_start_condition": {
                    "destination": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "manual_tag_start_condition": {
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    }
                },
                "name": "string",
                "pull_request_start_condition": {
                    "auto_cancel": True,
                    "destination": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                    "files_and_folders_rule": {
                        "matchers": [
                            {
                                "directory": "string",
                                "file_extension": "string",
                                "file_name": "string",
                            }
                        ],
                        "mode": "START_IF_ANY_FILE_MATCHES",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "scheduled_start_condition": {
                    "schedule": {
                        "days": ["SUNDAY"],
                        "frequency": "WEEKLY",
                        "hour": 123,
                        "minute": 123,
                        "timezone": "string",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "tag_start_condition": {
                    "auto_cancel": True,
                    "files_and_folders_rule": {
                        "matchers": [
                            {
                                "directory": "string",
                                "file_extension": "string",
                                "file_name": "string",
                            }
                        ],
                        "mode": "START_IF_ANY_FILE_MATCHES",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
            },
            "id": "string",
            "relationships": {
                "mac_os_version": {"data": {"id": "string", "type": "ciMacOsVersions"}},
                "xcode_version": {"data": {"id": "string", "type": "ciXcodeVersions"}},
            },
            "type": "ciWorkflows",
        }
    },
)
```

---

### 
> 

```python
client.v1.devices.patch(
    id="string",
    data={
        "data": {
            "attributes": {"name": "string", "status": "ENABLED"},
            "id": "string",
            "type": "devices",
        }
    },
)
```

---

### 
> 

```python
client.v1.end_user_license_agreements.patch(
    id="string",
    data={
        "data": {
            "attributes": {"agreement_text": "string"},
            "id": "string",
            "relationships": {
                "territories": {"data": [{"id": "string", "type": "territories"}]}
            },
            "type": "endUserLicenseAgreements",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_achievement_images.patch(
    id="string",
    data={
        "data": {
            "attributes": {"uploaded": True},
            "id": "string",
            "type": "gameCenterAchievementImages",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_achievement_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "after_earned_description": "string",
                "before_earned_description": "string",
                "name": "string",
            },
            "id": "string",
            "type": "gameCenterAchievementLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_achievements.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "archived": True,
                "points": 123,
                "reference_name": "string",
                "repeatable": True,
                "show_before_earned": True,
            },
            "id": "string",
            "type": "gameCenterAchievements",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_achievements.relationships.group_achievement.patch(
    id="string", data={"data": {"id": "string", "type": "gameCenterAchievements"}}
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.patch(
    id="string",
    data={
        "data": {
            "attributes": {"enabled": True},
            "id": "string",
            "type": "gameCenterAppVersions",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_details.patch(
    id="string",
    data={
        "data": {
            "attributes": {"challenge_enabled": True},
            "id": "string",
            "relationships": {
                "default_group_leaderboard": {
                    "data": {"id": "string", "type": "gameCenterLeaderboards"}
                },
                "default_leaderboard": {
                    "data": {"id": "string", "type": "gameCenterLeaderboards"}
                },
                "game_center_group": {
                    "data": {"id": "string", "type": "gameCenterGroups"}
                },
            },
            "type": "gameCenterDetails",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_details.relationships.game_center_achievements.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterAchievements"}]}
)
```

---

### 
> 

```python
client.v1.game_center_details.relationships.game_center_leaderboard_sets.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboardSets"}]}
)
```

---

### 
> 

```python
client.v1.game_center_details.relationships.game_center_leaderboards.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboards"}]}
)
```

---

### 
> 

```python
client.v1.game_center_enabled_versions.relationships.compatible_versions.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterEnabledVersions"}]}
)
```

---

### 
> 

```python
client.v1.game_center_groups.patch(
    id="string",
    data={
        "data": {
            "attributes": {"reference_name": "string"},
            "id": "string",
            "type": "gameCenterGroups",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_groups.relationships.game_center_achievements.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterAchievements"}]}
)
```

---

### 
> 

```python
client.v1.game_center_groups.relationships.game_center_leaderboard_sets.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboardSets"}]}
)
```

---

### 
> 

```python
client.v1.game_center_groups.relationships.game_center_leaderboards.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboards"}]}
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_images.patch(
    id="string",
    data={
        "data": {
            "attributes": {"uploaded": True},
            "id": "string",
            "type": "gameCenterLeaderboardImages",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "formatter_override": "INTEGER",
                "formatter_suffix": "string",
                "formatter_suffix_singular": "string",
                "name": "string",
            },
            "id": "string",
            "type": "gameCenterLeaderboardLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_images.patch(
    id="string",
    data={
        "data": {
            "attributes": {"uploaded": True},
            "id": "string",
            "type": "gameCenterLeaderboardSetImages",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"name": "string"},
            "id": "string",
            "type": "gameCenterLeaderboardSetLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_member_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"name": "string"},
            "id": "string",
            "type": "gameCenterLeaderboardSetMemberLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.patch(
    id="string",
    data={
        "data": {
            "attributes": {"reference_name": "string"},
            "id": "string",
            "type": "gameCenterLeaderboardSets",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.relationships.game_center_leaderboards.patch(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboards"}]}
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.relationships.group_leaderboard_set.patch(
    id="string", data={"data": {"id": "string", "type": "gameCenterLeaderboardSets"}}
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "archived": True,
                "default_formatter": "INTEGER",
                "recurrence_duration": "P3Y6M4DT12H30M5S",
                "recurrence_rule": "string",
                "recurrence_start_date": "1970-01-01T00:00:00",
                "reference_name": "string",
                "score_range_end": "string",
                "score_range_start": "string",
                "score_sort_type": "ASC",
                "submission_type": "BEST_SCORE",
            },
            "id": "string",
            "type": "gameCenterLeaderboards",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.relationships.group_leaderboard.patch(
    id="string", data={"data": {"id": "string", "type": "gameCenterLeaderboards"}}
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.patch(
    id="string",
    data={
        "data": {
            "attributes": {"classic_matchmaking_bundle_ids": ["string"]},
            "id": "string",
            "relationships": {
                "experiment_rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                },
                "rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                },
            },
            "type": "gameCenterMatchmakingQueues",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.patch(
    id="string",
    data={
        "data": {
            "attributes": {"max_players": 123, "min_players": 123},
            "id": "string",
            "type": "gameCenterMatchmakingRuleSets",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rules.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "description": "string",
                "expression": "string",
                "weight": 123.45,
            },
            "id": "string",
            "type": "gameCenterMatchmakingRules",
        }
    },
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_teams.patch(
    id="string",
    data={
        "data": {
            "attributes": {"max_players": 123, "min_players": 123},
            "id": "string",
            "type": "gameCenterMatchmakingTeams",
        }
    },
)
```

---

### 
> 

```python
client.v1.in_app_purchase_app_store_review_screenshots.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "inAppPurchaseAppStoreReviewScreenshots",
        }
    },
)
```

---

### 
> 

```python
client.v1.in_app_purchase_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"description": "string", "name": "string"},
            "id": "string",
            "type": "inAppPurchaseLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.marketplace_search_details.patch(
    id="string",
    data={
        "data": {
            "attributes": {"catalog_url": "http://www.example.com"},
            "id": "string",
            "type": "marketplaceSearchDetails",
        }
    },
)
```

---

### 
> 

```python
client.v1.marketplace_webhooks.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "endpoint_url": "http://www.example.com",
                "secret": "string",
            },
            "id": "string",
            "type": "marketplaceWebhooks",
        }
    },
)
```

---

### 
> 

```python
client.v1.promoted_purchase_images.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "promotedPurchaseImages",
        }
    },
)
```

---

### 
> 

```python
client.v1.promoted_purchases.patch(
    id="string",
    data={
        "data": {
            "attributes": {"enabled": True, "visible_for_all_users": True},
            "id": "string",
            "type": "promotedPurchases",
        }
    },
)
```

---

### 
> 

```python
client.v1.review_submission_items.patch(
    id="string",
    data={
        "data": {
            "attributes": {"removed": True, "resolved": True},
            "id": "string",
            "type": "reviewSubmissionItems",
        }
    },
)
```

---

### 
> 

```python
client.v1.review_submissions.patch(
    id="string",
    data={
        "data": {
            "attributes": {"canceled": True, "submitted": True},
            "id": "string",
            "type": "reviewSubmissions",
        }
    },
)
```

---

### 
> 

```python
client.v1.routing_app_coverages.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "routingAppCoverages",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_app_store_review_screenshots.patch(
    id="string",
    data={
        "data": {
            "attributes": {"source_file_checksum": "string", "uploaded": True},
            "id": "string",
            "type": "subscriptionAppStoreReviewScreenshots",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_grace_periods.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "duration": "THREE_DAYS",
                "opt_in": True,
                "renewal_type": "ALL_RENEWALS",
                "sandbox_opt_in": True,
            },
            "id": "string",
            "type": "subscriptionGracePeriods",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_group_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"custom_app_name": "string", "name": "string"},
            "id": "string",
            "type": "subscriptionGroupLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_groups.patch(
    id="string",
    data={
        "data": {
            "attributes": {"reference_name": "string"},
            "id": "string",
            "type": "subscriptionGroups",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_introductory_offers.patch(
    id="string",
    data={
        "data": {
            "attributes": {"end_date": "1970-01-01"},
            "id": "string",
            "type": "subscriptionIntroductoryOffers",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_localizations.patch(
    id="string",
    data={
        "data": {
            "attributes": {"description": "string", "name": "string"},
            "id": "string",
            "type": "subscriptionLocalizations",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_custom_codes.patch(
    id="string",
    data={
        "data": {
            "attributes": {"active": True},
            "id": "string",
            "type": "subscriptionOfferCodeCustomCodes",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_one_time_use_codes.patch(
    id="string",
    data={
        "data": {
            "attributes": {"active": True},
            "id": "string",
            "type": "subscriptionOfferCodeOneTimeUseCodes",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_offer_codes.patch(
    id="string",
    data={
        "data": {
            "attributes": {"active": True},
            "id": "string",
            "type": "subscriptionOfferCodes",
        }
    },
)
```

---

### 
> 

```python
client.v1.subscription_promotional_offers.patch(
    id="string",
    data={
        "data": {
            "id": "string",
            "relationships": {
                "prices": {
                    "data": [
                        {"id": "string", "type": "subscriptionPromotionalOfferPrices"}
                    ]
                }
            },
            "type": "subscriptionPromotionalOffers",
        },
        "included": [
            {
                "id": "string",
                "relationships": {
                    "subscription_price_point": {
                        "data": {"id": "string", "type": "subscriptionPricePoints"}
                    },
                    "territory": {"data": {"id": "string", "type": "territories"}},
                },
                "type": "subscriptionPromotionalOfferPrices",
            }
        ],
    },
)
```

---

### 
> 

```python
client.v1.subscriptions.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "family_sharable": True,
                "group_level": 123,
                "name": "string",
                "review_note": "string",
                "subscription_period": "ONE_WEEK",
            },
            "id": "string",
            "relationships": {
                "introductory_offers": {
                    "data": [{"id": "string", "type": "subscriptionIntroductoryOffers"}]
                },
                "prices": {"data": [{"id": "string", "type": "subscriptionPrices"}]},
                "promotional_offers": {
                    "data": [{"id": "string", "type": "subscriptionPromotionalOffers"}]
                },
            },
            "type": "subscriptions",
        },
        "included": [
            {
                "attributes": {
                    "duration": "ONE_DAY",
                    "name": "string",
                    "number_of_periods": 123,
                    "offer_code": "string",
                    "offer_mode": "PAY_AS_YOU_GO",
                },
                "id": "string",
                "relationships": {
                    "prices": {
                        "data": [
                            {
                                "id": "string",
                                "type": "subscriptionPromotionalOfferPrices",
                            }
                        ]
                    },
                    "subscription": {"data": {"id": "string", "type": "subscriptions"}},
                },
                "type": "subscriptionPromotionalOffers",
            }
        ],
    },
)
```

---

### 
> 

```python
client.v1.territory_availabilities.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "available": True,
                "pre_order_enabled": True,
                "release_date": "1970-01-01",
            },
            "id": "string",
            "type": "territoryAvailabilities",
        }
    },
)
```

---

### 
> 

```python
client.v1.users.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "all_apps_visible": True,
                "provisioning_allowed": True,
                "roles": ["ADMIN"],
            },
            "id": "string",
            "relationships": {
                "visible_apps": {"data": [{"id": "string", "type": "apps"}]}
            },
            "type": "users",
        }
    },
)
```

---

### 
> 

```python
client.v1.users.relationships.visible_apps.patch(
    id="string", data={"data": [{"id": "string", "type": "apps"}]}
)
```

---

### 
> 

```python
client.v2.app_store_version_experiments.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "name": "string",
                "started": True,
                "traffic_proportion": 123,
            },
            "id": "string",
            "type": "appStoreVersionExperiments",
        }
    },
)
```

---

### 
> 

```python
client.v2.in_app_purchases.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "family_sharable": True,
                "name": "string",
                "review_note": "string",
            },
            "id": "string",
            "type": "inAppPurchases",
        }
    },
)
```

---

### 
> 

```python
client.v2.sandbox_testers.patch(
    id="string",
    data={
        "data": {
            "attributes": {
                "interrupt_purchases": True,
                "subscription_renewal_rate": "MONTHLY_RENEWAL_EVERY_ONE_HOUR",
                "territory": "ABW",
            },
            "id": "string",
            "type": "sandboxTesters",
        }
    },
)
```

---

### 
> 

```python
client.v1.alternative_distribution_domains.create(
    data={
        "data": {
            "attributes": {"domain": "string", "reference_name": "string"},
            "type": "alternativeDistributionDomains",
        }
    }
)
```

---

### 
> 

```python
client.v1.alternative_distribution_keys.create(
    data={
        "data": {
            "attributes": {"public_key": "string"},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "alternativeDistributionKeys",
        }
    }
)
```

---

### 
> 

```python
client.v1.alternative_distribution_packages.create(
    data={
        "data": {
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "alternativeDistributionPackages",
        }
    }
)
```

---

### 
> 

```python
client.v1.analytics_report_requests.create(
    data={
        "data": {
            "attributes": {"access_type": "ONE_TIME_SNAPSHOT"},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "analyticsReportRequests",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_availabilities.create(
    data={
        "data": {
            "attributes": {"available_in_new_territories": True},
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "available_territories": {
                    "data": [{"id": "string", "type": "territories"}]
                },
            },
            "type": "appAvailabilities",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_clip_advanced_experience_images.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "type": "appClipAdvancedExperienceImages",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_clip_advanced_experiences.create(
    data={
        "data": {
            "attributes": {
                "action": "OPEN",
                "business_category": "AUTOMOTIVE",
                "default_language": "AR",
                "is_powered_by": True,
                "link": "http://www.example.com",
                "place": {
                    "categories": ["string"],
                    "display_point": {
                        "coordinates": {"latitude": 123.45, "longitude": 123.45},
                        "source": "CALCULATED",
                    },
                    "home_page": "string",
                    "main_address": {
                        "full_address": "string",
                        "structured_address": {
                            "country_code": "string",
                            "floor": "string",
                            "locality": "string",
                            "neighborhood": "string",
                            "postal_code": "string",
                            "state_province": "string",
                            "street_address": ["string"],
                        },
                    },
                    "map_action": "BUY_TICKETS",
                    "names": ["string"],
                    "phone_number": {
                        "intent": "string",
                        "number": "string",
                        "type": "FAX",
                    },
                    "place_id": "string",
                    "relationship": "OWNER",
                },
            },
            "relationships": {
                "app_clip": {"data": {"id": "string", "type": "appClips"}},
                "header_image": {
                    "data": {"id": "string", "type": "appClipAdvancedExperienceImages"}
                },
                "localizations": {
                    "data": [
                        {
                            "id": "string",
                            "type": "appClipAdvancedExperienceLocalizations",
                        }
                    ]
                },
            },
            "type": "appClipAdvancedExperiences",
        },
        "included": [
            {
                "attributes": {
                    "language": "AR",
                    "subtitle": "string",
                    "title": "string",
                },
                "id": "string",
                "type": "appClipAdvancedExperienceLocalizations",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.app_clip_app_store_review_details.create(
    data={
        "data": {
            "attributes": {"invocation_urls": ["http://www.example.com"]},
            "relationships": {
                "app_clip_default_experience": {
                    "data": {"id": "string", "type": "appClipDefaultExperiences"}
                }
            },
            "type": "appClipAppStoreReviewDetails",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_clip_default_experience_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string", "subtitle": "string"},
            "relationships": {
                "app_clip_default_experience": {
                    "data": {"id": "string", "type": "appClipDefaultExperiences"}
                }
            },
            "type": "appClipDefaultExperienceLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_clip_default_experiences.create(
    data={
        "data": {
            "attributes": {"action": "OPEN"},
            "relationships": {
                "app_clip": {"data": {"id": "string", "type": "appClips"}},
                "app_clip_default_experience_template": {
                    "data": {"id": "string", "type": "appClipDefaultExperiences"}
                },
                "release_with_app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                },
            },
            "type": "appClipDefaultExperiences",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_clip_header_images.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "app_clip_default_experience_localization": {
                    "data": {
                        "id": "string",
                        "type": "appClipDefaultExperienceLocalizations",
                    }
                }
            },
            "type": "appClipHeaderImages",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string", "promotional_text": "string"},
            "relationships": {
                "app_custom_product_page_version": {
                    "data": {"id": "string", "type": "appCustomProductPageVersions"}
                }
            },
            "type": "appCustomProductPageLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_custom_product_page_versions.create(
    data={
        "data": {
            "attributes": {"deep_link": "http://www.example.com"},
            "relationships": {
                "app_custom_product_page": {
                    "data": {"id": "string", "type": "appCustomProductPages"}
                },
                "app_custom_product_page_localizations": {
                    "data": [
                        {"id": "string", "type": "appCustomProductPageLocalizations"}
                    ]
                },
            },
            "type": "appCustomProductPageVersions",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_custom_product_pages.create(
    data={
        "data": {
            "attributes": {"name": "string"},
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "app_custom_product_page_versions": {
                    "data": [{"id": "string", "type": "appCustomProductPageVersions"}]
                },
                "app_store_version_template": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                },
                "custom_product_page_template": {
                    "data": {"id": "string", "type": "appCustomProductPages"}
                },
            },
            "type": "appCustomProductPages",
        },
        "included": [
            {
                "attributes": {"locale_field": "string", "promotional_text": "string"},
                "id": "string",
                "relationships": {
                    "app_custom_product_page_version": {
                        "data": {"id": "string", "type": "appCustomProductPageVersions"}
                    }
                },
                "type": "appCustomProductPageLocalizations",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.app_encryption_declaration_documents.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "app_encryption_declaration": {
                    "data": {"id": "string", "type": "appEncryptionDeclarations"}
                }
            },
            "type": "appEncryptionDeclarationDocuments",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_encryption_declarations.relationships.builds.create(
    id="string", data={"data": [{"id": "string", "type": "builds"}]}
)
```

---

### 
> 

```python
client.v1.app_event_localizations.create(
    data={
        "data": {
            "attributes": {
                "locale_field": "string",
                "long_description": "string",
                "name": "string",
                "short_description": "string",
            },
            "relationships": {
                "app_event": {"data": {"id": "string", "type": "appEvents"}}
            },
            "type": "appEventLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_event_screenshots.create(
    data={
        "data": {
            "attributes": {
                "app_event_asset_type": "EVENT_CARD",
                "file_name": "string",
                "file_size": 123,
            },
            "relationships": {
                "app_event_localization": {
                    "data": {"id": "string", "type": "appEventLocalizations"}
                }
            },
            "type": "appEventScreenshots",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_event_video_clips.create(
    data={
        "data": {
            "attributes": {
                "app_event_asset_type": "EVENT_CARD",
                "file_name": "string",
                "file_size": 123,
                "preview_frame_time_code": "string",
            },
            "relationships": {
                "app_event_localization": {
                    "data": {"id": "string", "type": "appEventLocalizations"}
                }
            },
            "type": "appEventVideoClips",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_events.create(
    data={
        "data": {
            "attributes": {
                "badge": "LIVE_EVENT",
                "deep_link": "http://www.example.com",
                "primary_locale": "string",
                "priority": "HIGH",
                "purchase_requirement": "NO_COST_ASSOCIATED",
                "purpose": "APPROPRIATE_FOR_ALL_USERS",
                "reference_name": "string",
                "territory_schedules": [
                    {
                        "event_end": "1970-01-01T00:00:00",
                        "event_start": "1970-01-01T00:00:00",
                        "publish_start": "1970-01-01T00:00:00",
                        "territories": ["string"],
                    }
                ],
            },
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "appEvents",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_info_localizations.create(
    data={
        "data": {
            "attributes": {
                "locale_field": "string",
                "name": "string",
                "privacy_choices_url": "string",
                "privacy_policy_text": "string",
                "privacy_policy_url": "string",
                "subtitle": "string",
            },
            "relationships": {
                "app_info": {"data": {"id": "string", "type": "appInfos"}}
            },
            "type": "appInfoLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_pre_orders.create(
    data={
        "data": {
            "attributes": {"app_release_date": "1970-01-01"},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "appPreOrders",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_preview_sets.create(
    data={
        "data": {
            "attributes": {"preview_type": "IPHONE_67"},
            "relationships": {
                "app_custom_product_page_localization": {
                    "data": {
                        "id": "string",
                        "type": "appCustomProductPageLocalizations",
                    }
                },
                "app_store_version_experiment_treatment_localization": {
                    "data": {
                        "id": "string",
                        "type": "appStoreVersionExperimentTreatmentLocalizations",
                    }
                },
                "app_store_version_localization": {
                    "data": {"id": "string", "type": "appStoreVersionLocalizations"}
                },
            },
            "type": "appPreviewSets",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_previews.create(
    data={
        "data": {
            "attributes": {
                "file_name": "string",
                "file_size": 123,
                "mime_type": "string",
                "preview_frame_time_code": "string",
            },
            "relationships": {
                "app_preview_set": {"data": {"id": "string", "type": "appPreviewSets"}}
            },
            "type": "appPreviews",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_price_schedules.create(
    data={
        "data": {
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "base_territory": {"data": {"id": "string", "type": "territories"}},
                "manual_prices": {"data": [{"id": "string", "type": "appPrices"}]},
            },
            "type": "appPriceSchedules",
        },
        "included": [{"id": "string", "type": "appPrices"}],
    }
)
```

---

### 
> 

```python
client.v1.app_screenshot_sets.create(
    data={
        "data": {
            "attributes": {"screenshot_display_type": "APP_IPHONE_67"},
            "relationships": {
                "app_custom_product_page_localization": {
                    "data": {
                        "id": "string",
                        "type": "appCustomProductPageLocalizations",
                    }
                },
                "app_store_version_experiment_treatment_localization": {
                    "data": {
                        "id": "string",
                        "type": "appStoreVersionExperimentTreatmentLocalizations",
                    }
                },
                "app_store_version_localization": {
                    "data": {"id": "string", "type": "appStoreVersionLocalizations"}
                },
            },
            "type": "appScreenshotSets",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_screenshots.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "app_screenshot_set": {
                    "data": {"id": "string", "type": "appScreenshotSets"}
                }
            },
            "type": "appScreenshots",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_review_attachments.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "app_store_review_detail": {
                    "data": {"id": "string", "type": "appStoreReviewDetails"}
                }
            },
            "type": "appStoreReviewAttachments",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_review_details.create(
    data={
        "data": {
            "attributes": {
                "contact_email": "string",
                "contact_first_name": "string",
                "contact_last_name": "string",
                "contact_phone": "string",
                "demo_account_name": "string",
                "demo_account_password": "string",
                "demo_account_required": True,
                "notes": "string",
            },
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appStoreReviewDetails",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatment_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string"},
            "relationships": {
                "app_store_version_experiment_treatment": {
                    "data": {
                        "id": "string",
                        "type": "appStoreVersionExperimentTreatments",
                    }
                }
            },
            "type": "appStoreVersionExperimentTreatmentLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_experiment_treatments.create(
    data={
        "data": {
            "attributes": {"app_icon_name": "string", "name": "string"},
            "relationships": {
                "app_store_version_experiment": {
                    "data": {"id": "string", "type": "appStoreVersionExperiments"}
                },
                "app_store_version_experiment_v2": {
                    "data": {"id": "string", "type": "appStoreVersionExperiments"}
                },
            },
            "type": "appStoreVersionExperimentTreatments",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_experiments.create(
    data={
        "data": {
            "attributes": {"name": "string", "traffic_proportion": 123},
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appStoreVersionExperiments",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_localizations.create(
    data={
        "data": {
            "attributes": {
                "description": "string",
                "keywords": "string",
                "locale_field": "string",
                "marketing_url": "http://www.example.com",
                "promotional_text": "string",
                "support_url": "http://www.example.com",
                "whats_new": "string",
            },
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appStoreVersionLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_phased_releases.create(
    data={
        "data": {
            "attributes": {"phased_release_state": "INACTIVE"},
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appStoreVersionPhasedReleases",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_promotions.create(
    data={
        "data": {
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                },
                "app_store_version_experiment_treatment": {
                    "data": {
                        "id": "string",
                        "type": "appStoreVersionExperimentTreatments",
                    }
                },
            },
            "type": "appStoreVersionPromotions",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_release_requests.create(
    data={
        "data": {
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appStoreVersionReleaseRequests",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_version_submissions.create(
    data={
        "data": {
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "appStoreVersionSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.app_store_versions.create(
    data={
        "data": {
            "attributes": {
                "copyright": "string",
                "earliest_release_date": "1970-01-01T00:00:00",
                "platform_field": "IOS",
                "release_type": "MANUAL",
                "review_type": "APP_STORE",
                "version_string": "string",
            },
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "app_store_version_localizations": {
                    "data": [{"id": "string", "type": "appStoreVersionLocalizations"}]
                },
                "build": {"data": {"id": "string", "type": "builds"}},
            },
            "type": "appStoreVersions",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_app_clip_invocation_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string", "title": "string"},
            "relationships": {
                "beta_app_clip_invocation": {
                    "data": {"id": "string", "type": "betaAppClipInvocations"}
                }
            },
            "type": "betaAppClipInvocationLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_app_clip_invocations.create(
    data={
        "data": {
            "attributes": {"url": "http://www.example.com"},
            "relationships": {
                "beta_app_clip_invocation_localizations": {
                    "data": [
                        {"id": "string", "type": "betaAppClipInvocationLocalizations"}
                    ]
                },
                "build_bundle": {"data": {"id": "string", "type": "buildBundles"}},
            },
            "type": "betaAppClipInvocations",
        },
        "included": [
            {
                "attributes": {"locale_field": "string", "title": "string"},
                "id": "string",
                "relationships": {
                    "beta_app_clip_invocation": {
                        "data": {"id": "string", "type": "betaAppClipInvocations"}
                    }
                },
                "type": "betaAppClipInvocationLocalizations",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.beta_app_localizations.create(
    data={
        "data": {
            "attributes": {
                "description": "string",
                "feedback_email": "string",
                "locale_field": "string",
                "marketing_url": "string",
                "privacy_policy_url": "string",
                "tv_os_privacy_policy": "string",
            },
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "betaAppLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_app_review_submissions.create(
    data={
        "data": {
            "relationships": {"build": {"data": {"id": "string", "type": "builds"}}},
            "type": "betaAppReviewSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_build_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string", "whats_new": "string"},
            "relationships": {"build": {"data": {"id": "string", "type": "builds"}}},
            "type": "betaBuildLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_groups.create(
    data={
        "data": {
            "attributes": {
                "feedback_enabled": True,
                "has_access_to_all_builds": True,
                "is_internal_group": True,
                "name": "string",
                "public_link_enabled": True,
                "public_link_limit": 123,
                "public_link_limit_enabled": True,
            },
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "beta_testers": {"data": [{"id": "string", "type": "betaTesters"}]},
                "builds": {"data": [{"id": "string", "type": "builds"}]},
            },
            "type": "betaGroups",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_groups.relationships.beta_testers.create(
    id="string", data={"data": [{"id": "string", "type": "betaTesters"}]}
)
```

---

### 
> 

```python
client.v1.beta_groups.relationships.builds.create(
    id="string", data={"data": [{"id": "string", "type": "builds"}]}
)
```

---

### 
> 

```python
client.v1.beta_tester_invitations.create(
    data={
        "data": {
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "beta_tester": {"data": {"id": "string", "type": "betaTesters"}},
            },
            "type": "betaTesterInvitations",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_testers.create(
    data={
        "data": {
            "attributes": {
                "email_field": "mail@example.com",
                "first_name": "string",
                "last_name": "string",
            },
            "relationships": {
                "beta_groups": {"data": [{"id": "string", "type": "betaGroups"}]},
                "builds": {"data": [{"id": "string", "type": "builds"}]},
            },
            "type": "betaTesters",
        }
    }
)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.beta_groups.create(
    id="string", data={"data": [{"id": "string", "type": "betaGroups"}]}
)
```

---

### 
> 

```python
client.v1.beta_testers.relationships.builds.create(
    id="string", data={"data": [{"id": "string", "type": "builds"}]}
)
```

---

### 
> 

```python
client.v1.build_beta_notifications.create(
    data={
        "data": {
            "relationships": {"build": {"data": {"id": "string", "type": "builds"}}},
            "type": "buildBetaNotifications",
        }
    }
)
```

---

### 
> 

```python
client.v1.builds.relationships.beta_groups.create(
    id="string", data={"data": [{"id": "string", "type": "betaGroups"}]}
)
```

---

### 
> 

```python
client.v1.builds.relationships.individual_testers.create(
    id="string", data={"data": [{"id": "string", "type": "betaTesters"}]}
)
```

---

### 
> 

```python
client.v1.bundle_id_capabilities.create(
    data={
        "data": {
            "attributes": {
                "capability_type": "ICLOUD",
                "settings": [
                    {
                        "allowed_instances": "ENTRY",
                        "description": "string",
                        "enabled_by_default": True,
                        "key": "ICLOUD_VERSION",
                        "min_instances": 123,
                        "name": "string",
                        "options": [
                            {
                                "description": "string",
                                "enabled": True,
                                "enabled_by_default": True,
                                "key": "XCODE_5",
                                "name": "string",
                                "supports_wildcard": True,
                            }
                        ],
                        "visible": True,
                    }
                ],
            },
            "relationships": {
                "bundle_id": {"data": {"id": "string", "type": "bundleIds"}}
            },
            "type": "bundleIdCapabilities",
        }
    }
)
```

---

### 
> 

```python
client.v1.bundle_ids.create(
    data={
        "data": {
            "attributes": {
                "identifier": "string",
                "name": "string",
                "platform_field": "IOS",
                "seed_id": "string",
            },
            "type": "bundleIds",
        }
    }
)
```

---

### 
> 

```python
client.v1.certificates.create(
    data={
        "data": {
            "attributes": {
                "certificate_type": "IOS_DEVELOPMENT",
                "csr_content": "string",
            },
            "type": "certificates",
        }
    }
)
```

---

### 
> 

```python
client.v1.ci_build_runs.create(
    data={
        "data": {
            "attributes": {"clean": True},
            "relationships": {
                "build_run": {"data": {"id": "string", "type": "ciBuildRuns"}},
                "pull_request": {"data": {"id": "string", "type": "scmPullRequests"}},
                "source_branch_or_tag": {
                    "data": {"id": "string", "type": "scmGitReferences"}
                },
                "workflow": {"data": {"id": "string", "type": "ciWorkflows"}},
            },
            "type": "ciBuildRuns",
        }
    }
)
```

---

### 
> 

```python
client.v1.ci_workflows.create(
    data={
        "data": {
            "attributes": {
                "actions": [
                    {
                        "action_type": "BUILD",
                        "build_distribution_audience": "INTERNAL_ONLY",
                        "destination": "ANY_IOS_DEVICE",
                        "is_required_to_pass": True,
                        "name": "string",
                        "platform_field": "MACOS",
                        "scheme": "string",
                        "test_configuration": {
                            "kind": "USE_SCHEME_SETTINGS",
                            "test_destinations": [
                                {
                                    "device_type_identifier": "string",
                                    "device_type_name": "string",
                                    "kind": "SIMULATOR",
                                    "runtime_identifier": "string",
                                    "runtime_name": "string",
                                }
                            ],
                            "test_plan_name": "string",
                        },
                    }
                ],
                "branch_start_condition": {
                    "auto_cancel": True,
                    "files_and_folders_rule": {
                        "matchers": [
                            {
                                "directory": "string",
                                "file_extension": "string",
                                "file_name": "string",
                            }
                        ],
                        "mode": "START_IF_ANY_FILE_MATCHES",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "clean": True,
                "container_file_path": "string",
                "description": "string",
                "is_enabled": True,
                "is_locked_for_editing": True,
                "manual_branch_start_condition": {
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    }
                },
                "manual_pull_request_start_condition": {
                    "destination": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "manual_tag_start_condition": {
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    }
                },
                "name": "string",
                "pull_request_start_condition": {
                    "auto_cancel": True,
                    "destination": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                    "files_and_folders_rule": {
                        "matchers": [
                            {
                                "directory": "string",
                                "file_extension": "string",
                                "file_name": "string",
                            }
                        ],
                        "mode": "START_IF_ANY_FILE_MATCHES",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "scheduled_start_condition": {
                    "schedule": {
                        "days": ["SUNDAY"],
                        "frequency": "WEEKLY",
                        "hour": 123,
                        "minute": 123,
                        "timezone": "string",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
                "tag_start_condition": {
                    "auto_cancel": True,
                    "files_and_folders_rule": {
                        "matchers": [
                            {
                                "directory": "string",
                                "file_extension": "string",
                                "file_name": "string",
                            }
                        ],
                        "mode": "START_IF_ANY_FILE_MATCHES",
                    },
                    "source": {
                        "is_all_match": True,
                        "patterns": [{"is_prefix": True, "pattern": "string"}],
                    },
                },
            },
            "relationships": {
                "mac_os_version": {"data": {"id": "string", "type": "ciMacOsVersions"}},
                "product": {"data": {"id": "string", "type": "ciProducts"}},
                "repository": {"data": {"id": "string", "type": "scmRepositories"}},
                "xcode_version": {"data": {"id": "string", "type": "ciXcodeVersions"}},
            },
            "type": "ciWorkflows",
        }
    }
)
```

---

### 
> 

```python
client.v1.customer_review_responses.create(
    data={
        "data": {
            "attributes": {"response_body": "string"},
            "relationships": {
                "review": {"data": {"id": "string", "type": "customerReviews"}}
            },
            "type": "customerReviewResponses",
        }
    }
)
```

---

### 
> 

```python
client.v1.devices.create(
    data={
        "data": {
            "attributes": {"name": "string", "platform_field": "IOS", "udid": "string"},
            "type": "devices",
        }
    }
)
```

---

### 
> 

```python
client.v1.end_app_availability_pre_orders.create(
    data={
        "data": {
            "relationships": {
                "territory_availabilities": {
                    "data": [{"id": "string", "type": "territoryAvailabilities"}]
                }
            },
            "type": "endAppAvailabilityPreOrders",
        }
    }
)
```

---

### 
> 

```python
client.v1.end_user_license_agreements.create(
    data={
        "data": {
            "attributes": {"agreement_text": "string"},
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "territories": {"data": [{"id": "string", "type": "territories"}]},
            },
            "type": "endUserLicenseAgreements",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_achievement_images.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "game_center_achievement_localization": {
                    "data": {
                        "id": "string",
                        "type": "gameCenterAchievementLocalizations",
                    }
                }
            },
            "type": "gameCenterAchievementImages",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_achievement_localizations.create(
    data={
        "data": {
            "attributes": {
                "after_earned_description": "string",
                "before_earned_description": "string",
                "locale_field": "string",
                "name": "string",
            },
            "relationships": {
                "game_center_achievement": {
                    "data": {"id": "string", "type": "gameCenterAchievements"}
                }
            },
            "type": "gameCenterAchievementLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_achievement_releases.create(
    data={
        "data": {
            "relationships": {
                "game_center_achievement": {
                    "data": {"id": "string", "type": "gameCenterAchievements"}
                },
                "game_center_detail": {
                    "data": {"id": "string", "type": "gameCenterDetails"}
                },
            },
            "type": "gameCenterAchievementReleases",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_achievements.create(
    data={
        "data": {
            "attributes": {
                "points": 123,
                "reference_name": "string",
                "repeatable": True,
                "show_before_earned": True,
                "vendor_identifier": "string",
            },
            "relationships": {
                "game_center_detail": {
                    "data": {"id": "string", "type": "gameCenterDetails"}
                },
                "game_center_group": {
                    "data": {"id": "string", "type": "gameCenterGroups"}
                },
            },
            "type": "gameCenterAchievements",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.create(
    data={
        "data": {
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "gameCenterAppVersions",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_app_versions.relationships.compatibility_versions.create(
    id="string", data={"data": [{"id": "string", "type": "gameCenterAppVersions"}]}
)
```

---

### 
> 

```python
client.v1.game_center_details.create(
    data={
        "data": {
            "attributes": {"challenge_enabled": True},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "gameCenterDetails",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_enabled_versions.relationships.compatible_versions.create(
    id="string", data={"data": [{"id": "string", "type": "gameCenterEnabledVersions"}]}
)
```

---

### 
> 

```python
client.v1.game_center_groups.create(
    data={
        "data": {"attributes": {"reference_name": "string"}, "type": "gameCenterGroups"}
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_entry_submissions.create(
    data={
        "data": {
            "attributes": {
                "bundle_id": "string",
                "challenge_ids": ["string"],
                "context": "string",
                "scoped_player_id": "string",
                "score": "string",
                "submitted_date": "1970-01-01T00:00:00",
                "vendor_identifier": "string",
            },
            "type": "gameCenterLeaderboardEntrySubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_images.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "game_center_leaderboard_localization": {
                    "data": {
                        "id": "string",
                        "type": "gameCenterLeaderboardLocalizations",
                    }
                }
            },
            "type": "gameCenterLeaderboardImages",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_localizations.create(
    data={
        "data": {
            "attributes": {
                "formatter_override": "INTEGER",
                "formatter_suffix": "string",
                "formatter_suffix_singular": "string",
                "locale_field": "string",
                "name": "string",
            },
            "relationships": {
                "game_center_leaderboard": {
                    "data": {"id": "string", "type": "gameCenterLeaderboards"}
                }
            },
            "type": "gameCenterLeaderboardLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_releases.create(
    data={
        "data": {
            "relationships": {
                "game_center_detail": {
                    "data": {"id": "string", "type": "gameCenterDetails"}
                },
                "game_center_leaderboard": {
                    "data": {"id": "string", "type": "gameCenterLeaderboards"}
                },
            },
            "type": "gameCenterLeaderboardReleases",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_images.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "game_center_leaderboard_set_localization": {
                    "data": {
                        "id": "string",
                        "type": "gameCenterLeaderboardSetLocalizations",
                    }
                }
            },
            "type": "gameCenterLeaderboardSetImages",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string", "name": "string"},
            "relationships": {
                "game_center_leaderboard_set": {
                    "data": {"id": "string", "type": "gameCenterLeaderboardSets"}
                }
            },
            "type": "gameCenterLeaderboardSetLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_member_localizations.create(
    data={
        "data": {
            "attributes": {"locale_field": "string", "name": "string"},
            "relationships": {
                "game_center_leaderboard": {
                    "data": {"id": "string", "type": "gameCenterLeaderboards"}
                },
                "game_center_leaderboard_set": {
                    "data": {"id": "string", "type": "gameCenterLeaderboardSets"}
                },
            },
            "type": "gameCenterLeaderboardSetMemberLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_set_releases.create(
    data={
        "data": {
            "relationships": {
                "game_center_detail": {
                    "data": {"id": "string", "type": "gameCenterDetails"}
                },
                "game_center_leaderboard_set": {
                    "data": {"id": "string", "type": "gameCenterLeaderboardSets"}
                },
            },
            "type": "gameCenterLeaderboardSetReleases",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.create(
    data={
        "data": {
            "attributes": {"reference_name": "string", "vendor_identifier": "string"},
            "relationships": {
                "game_center_detail": {
                    "data": {"id": "string", "type": "gameCenterDetails"}
                },
                "game_center_group": {
                    "data": {"id": "string", "type": "gameCenterGroups"}
                },
                "game_center_leaderboards": {
                    "data": [{"id": "string", "type": "gameCenterLeaderboards"}]
                },
            },
            "type": "gameCenterLeaderboardSets",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_leaderboard_sets.relationships.game_center_leaderboards.create(
    id="string", data={"data": [{"id": "string", "type": "gameCenterLeaderboards"}]}
)
```

---

### 
> 

```python
client.v1.game_center_leaderboards.create(
    data={
        "data": {
            "attributes": {
                "default_formatter": "INTEGER",
                "recurrence_duration": "P3Y6M4DT12H30M5S",
                "recurrence_rule": "string",
                "recurrence_start_date": "1970-01-01T00:00:00",
                "reference_name": "string",
                "score_range_end": "string",
                "score_range_start": "string",
                "score_sort_type": "ASC",
                "submission_type": "BEST_SCORE",
                "vendor_identifier": "string",
            },
            "relationships": {
                "game_center_detail": {
                    "data": {"id": "string", "type": "gameCenterDetails"}
                },
                "game_center_group": {
                    "data": {"id": "string", "type": "gameCenterGroups"}
                },
                "game_center_leaderboard_sets": {
                    "data": [{"id": "string", "type": "gameCenterLeaderboardSets"}]
                },
            },
            "type": "gameCenterLeaderboards",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_queues.create(
    data={
        "data": {
            "attributes": {
                "classic_matchmaking_bundle_ids": ["string"],
                "reference_name": "string",
            },
            "relationships": {
                "experiment_rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                },
                "rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                },
            },
            "type": "gameCenterMatchmakingQueues",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_set_tests.create(
    data={
        "data": {
            "relationships": {
                "matchmaking_requests": {
                    "data": [
                        {"id": "string", "type": "gameCenterMatchmakingTestRequests"}
                    ]
                },
                "matchmaking_rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                },
            },
            "type": "gameCenterMatchmakingRuleSetTests",
        },
        "included": [
            {
                "attributes": {
                    "player_id": "string",
                    "properties": [{"key": "string", "value": "string"}],
                },
                "id": "string",
                "type": "gameCenterMatchmakingTestPlayerProperties",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rule_sets.create(
    data={
        "data": {
            "attributes": {
                "max_players": 123,
                "min_players": 123,
                "reference_name": "string",
                "rule_language_version": 123,
            },
            "type": "gameCenterMatchmakingRuleSets",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_rules.create(
    data={
        "data": {
            "attributes": {
                "description": "string",
                "expression": "string",
                "reference_name": "string",
                "type": "COMPATIBLE",
                "weight": 123.45,
            },
            "relationships": {
                "rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                }
            },
            "type": "gameCenterMatchmakingRules",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_matchmaking_teams.create(
    data={
        "data": {
            "attributes": {
                "max_players": 123,
                "min_players": 123,
                "reference_name": "string",
            },
            "relationships": {
                "rule_set": {
                    "data": {"id": "string", "type": "gameCenterMatchmakingRuleSets"}
                }
            },
            "type": "gameCenterMatchmakingTeams",
        }
    }
)
```

---

### 
> 

```python
client.v1.game_center_player_achievement_submissions.create(
    data={
        "data": {
            "attributes": {
                "bundle_id": "string",
                "challenge_ids": ["string"],
                "percentage_achieved": 123,
                "scoped_player_id": "string",
                "submitted_date": "1970-01-01T00:00:00",
                "vendor_identifier": "string",
            },
            "type": "gameCenterPlayerAchievementSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.in_app_purchase_app_store_review_screenshots.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "in_app_purchase_v2": {
                    "data": {"id": "string", "type": "inAppPurchases"}
                }
            },
            "type": "inAppPurchaseAppStoreReviewScreenshots",
        }
    }
)
```

---

### 
> 

```python
client.v1.in_app_purchase_availabilities.create(
    data={
        "data": {
            "attributes": {"available_in_new_territories": True},
            "relationships": {
                "available_territories": {
                    "data": [{"id": "string", "type": "territories"}]
                },
                "in_app_purchase": {"data": {"id": "string", "type": "inAppPurchases"}},
            },
            "type": "inAppPurchaseAvailabilities",
        }
    }
)
```

---

### 
> 

```python
client.v1.in_app_purchase_localizations.create(
    data={
        "data": {
            "attributes": {
                "description": "string",
                "locale_field": "string",
                "name": "string",
            },
            "relationships": {
                "in_app_purchase_v2": {
                    "data": {"id": "string", "type": "inAppPurchases"}
                }
            },
            "type": "inAppPurchaseLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.in_app_purchase_price_schedules.create(
    data={
        "data": {
            "relationships": {
                "base_territory": {"data": {"id": "string", "type": "territories"}},
                "in_app_purchase": {"data": {"id": "string", "type": "inAppPurchases"}},
                "manual_prices": {
                    "data": [{"id": "string", "type": "inAppPurchasePrices"}]
                },
            },
            "type": "inAppPurchasePriceSchedules",
        },
        "included": [
            {
                "attributes": {"end_date": "1970-01-01", "start_date": "1970-01-01"},
                "id": "string",
                "relationships": {
                    "in_app_purchase_price_point": {
                        "data": {"id": "string", "type": "inAppPurchasePricePoints"}
                    },
                    "in_app_purchase_v2": {
                        "data": {"id": "string", "type": "inAppPurchases"}
                    },
                },
                "type": "inAppPurchasePrices",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.in_app_purchase_submissions.create(
    data={
        "data": {
            "relationships": {
                "in_app_purchase_v2": {
                    "data": {"id": "string", "type": "inAppPurchases"}
                }
            },
            "type": "inAppPurchaseSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.marketplace_domains.create(
    data={
        "data": {
            "attributes": {"domain": "string", "reference_name": "string"},
            "type": "marketplaceDomains",
        }
    }
)
```

---

### 
> 

```python
client.v1.marketplace_search_details.create(
    data={
        "data": {
            "attributes": {"catalog_url": "http://www.example.com"},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "marketplaceSearchDetails",
        }
    }
)
```

---

### 
> 

```python
client.v1.marketplace_webhooks.create(
    data={
        "data": {
            "attributes": {
                "endpoint_url": "http://www.example.com",
                "secret": "string",
            },
            "type": "marketplaceWebhooks",
        }
    }
)
```

---

### 
> 

```python
client.v1.profiles.create(
    data={
        "data": {
            "attributes": {"name": "string", "profile_type": "IOS_APP_DEVELOPMENT"},
            "relationships": {
                "bundle_id": {"data": {"id": "string", "type": "bundleIds"}},
                "certificates": {"data": [{"id": "string", "type": "certificates"}]},
                "devices": {"data": [{"id": "string", "type": "devices"}]},
            },
            "type": "profiles",
        }
    }
)
```

---

### 
> 

```python
client.v1.promoted_purchase_images.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "promoted_purchase": {
                    "data": {"id": "string", "type": "promotedPurchases"}
                }
            },
            "type": "promotedPurchaseImages",
        }
    }
)
```

---

### 
> 

```python
client.v1.promoted_purchases.create(
    data={
        "data": {
            "attributes": {"enabled": True, "visible_for_all_users": True},
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "in_app_purchase_v2": {
                    "data": {"id": "string", "type": "inAppPurchases"}
                },
                "subscription": {"data": {"id": "string", "type": "subscriptions"}},
            },
            "type": "promotedPurchases",
        }
    }
)
```

---

### 
> 

```python
client.v1.review_submission_items.create(
    data={
        "data": {
            "relationships": {
                "app_custom_product_page_version": {
                    "data": {"id": "string", "type": "appCustomProductPageVersions"}
                },
                "app_event": {"data": {"id": "string", "type": "appEvents"}},
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                },
                "app_store_version_experiment": {
                    "data": {"id": "string", "type": "appStoreVersionExperiments"}
                },
                "app_store_version_experiment_v2": {
                    "data": {"id": "string", "type": "appStoreVersionExperiments"}
                },
                "review_submission": {
                    "data": {"id": "string", "type": "reviewSubmissions"}
                },
            },
            "type": "reviewSubmissionItems",
        }
    }
)
```

---

### 
> 

```python
client.v1.review_submissions.create(
    data={
        "data": {
            "attributes": {"platform_field": "IOS"},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "reviewSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.routing_app_coverages.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "app_store_version": {
                    "data": {"id": "string", "type": "appStoreVersions"}
                }
            },
            "type": "routingAppCoverages",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_app_store_review_screenshots.create(
    data={
        "data": {
            "attributes": {"file_name": "string", "file_size": 123},
            "relationships": {
                "subscription": {"data": {"id": "string", "type": "subscriptions"}}
            },
            "type": "subscriptionAppStoreReviewScreenshots",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_availabilities.create(
    data={
        "data": {
            "attributes": {"available_in_new_territories": True},
            "relationships": {
                "available_territories": {
                    "data": [{"id": "string", "type": "territories"}]
                },
                "subscription": {"data": {"id": "string", "type": "subscriptions"}},
            },
            "type": "subscriptionAvailabilities",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_group_localizations.create(
    data={
        "data": {
            "attributes": {
                "custom_app_name": "string",
                "locale_field": "string",
                "name": "string",
            },
            "relationships": {
                "subscription_group": {
                    "data": {"id": "string", "type": "subscriptionGroups"}
                }
            },
            "type": "subscriptionGroupLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_group_submissions.create(
    data={
        "data": {
            "relationships": {
                "subscription_group": {
                    "data": {"id": "string", "type": "subscriptionGroups"}
                }
            },
            "type": "subscriptionGroupSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_groups.create(
    data={
        "data": {
            "attributes": {"reference_name": "string"},
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "subscriptionGroups",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_introductory_offers.create(
    data={
        "data": {
            "attributes": {
                "duration": "ONE_DAY",
                "end_date": "1970-01-01",
                "number_of_periods": 123,
                "offer_mode": "PAY_AS_YOU_GO",
                "start_date": "1970-01-01",
            },
            "relationships": {
                "subscription": {"data": {"id": "string", "type": "subscriptions"}},
                "subscription_price_point": {
                    "data": {"id": "string", "type": "subscriptionPricePoints"}
                },
                "territory": {"data": {"id": "string", "type": "territories"}},
            },
            "type": "subscriptionIntroductoryOffers",
        },
        "included": [{"id": "string", "type": "subscriptionPricePoints"}],
    }
)
```

---

### 
> 

```python
client.v1.subscription_localizations.create(
    data={
        "data": {
            "attributes": {
                "description": "string",
                "locale_field": "string",
                "name": "string",
            },
            "relationships": {
                "subscription": {"data": {"id": "string", "type": "subscriptions"}}
            },
            "type": "subscriptionLocalizations",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_custom_codes.create(
    data={
        "data": {
            "attributes": {
                "custom_code": "string",
                "expiration_date": "1970-01-01",
                "number_of_codes": 123,
            },
            "relationships": {
                "offer_code": {
                    "data": {"id": "string", "type": "subscriptionOfferCodes"}
                }
            },
            "type": "subscriptionOfferCodeCustomCodes",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_offer_code_one_time_use_codes.create(
    data={
        "data": {
            "attributes": {"expiration_date": "1970-01-01", "number_of_codes": 123},
            "relationships": {
                "offer_code": {
                    "data": {"id": "string", "type": "subscriptionOfferCodes"}
                }
            },
            "type": "subscriptionOfferCodeOneTimeUseCodes",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_offer_codes.create(
    data={
        "data": {
            "attributes": {
                "customer_eligibilities": ["NEW"],
                "duration": "ONE_DAY",
                "name": "string",
                "number_of_periods": 123,
                "offer_eligibility": "STACK_WITH_INTRO_OFFERS",
                "offer_mode": "PAY_AS_YOU_GO",
            },
            "relationships": {
                "prices": {
                    "data": [{"id": "string", "type": "subscriptionOfferCodePrices"}]
                },
                "subscription": {"data": {"id": "string", "type": "subscriptions"}},
            },
            "type": "subscriptionOfferCodes",
        },
        "included": [
            {
                "id": "string",
                "relationships": {
                    "subscription_price_point": {
                        "data": {"id": "string", "type": "subscriptionPricePoints"}
                    },
                    "territory": {"data": {"id": "string", "type": "territories"}},
                },
                "type": "subscriptionOfferCodePrices",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.subscription_prices.create(
    data={
        "data": {
            "attributes": {"preserve_current_price": True, "start_date": "1970-01-01"},
            "relationships": {
                "subscription": {"data": {"id": "string", "type": "subscriptions"}},
                "subscription_price_point": {
                    "data": {"id": "string", "type": "subscriptionPricePoints"}
                },
                "territory": {"data": {"id": "string", "type": "territories"}},
            },
            "type": "subscriptionPrices",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscription_promotional_offers.create(
    data={
        "data": {
            "attributes": {
                "duration": "ONE_DAY",
                "name": "string",
                "number_of_periods": 123,
                "offer_code": "string",
                "offer_mode": "PAY_AS_YOU_GO",
            },
            "relationships": {
                "prices": {
                    "data": [
                        {"id": "string", "type": "subscriptionPromotionalOfferPrices"}
                    ]
                },
                "subscription": {"data": {"id": "string", "type": "subscriptions"}},
            },
            "type": "subscriptionPromotionalOffers",
        },
        "included": [
            {
                "id": "string",
                "relationships": {
                    "subscription_price_point": {
                        "data": {"id": "string", "type": "subscriptionPricePoints"}
                    },
                    "territory": {"data": {"id": "string", "type": "territories"}},
                },
                "type": "subscriptionPromotionalOfferPrices",
            }
        ],
    }
)
```

---

### 
> 

```python
client.v1.subscription_submissions.create(
    data={
        "data": {
            "relationships": {
                "subscription": {"data": {"id": "string", "type": "subscriptions"}}
            },
            "type": "subscriptionSubmissions",
        }
    }
)
```

---

### 
> 

```python
client.v1.subscriptions.create(
    data={
        "data": {
            "attributes": {
                "family_sharable": True,
                "group_level": 123,
                "name": "string",
                "product_id": "string",
                "review_note": "string",
                "subscription_period": "ONE_WEEK",
            },
            "relationships": {
                "group": {"data": {"id": "string", "type": "subscriptionGroups"}}
            },
            "type": "subscriptions",
        }
    }
)
```

---

### 
> 

```python
client.v1.user_invitations.create(
    data={
        "data": {
            "attributes": {
                "all_apps_visible": True,
                "email_field": "mail@example.com",
                "first_name": "string",
                "last_name": "string",
                "provisioning_allowed": True,
                "roles": ["ADMIN"],
            },
            "relationships": {
                "visible_apps": {"data": [{"id": "string", "type": "apps"}]}
            },
            "type": "userInvitations",
        }
    }
)
```

---

### 
> 

```python
client.v1.users.relationships.visible_apps.create(
    id="string", data={"data": [{"id": "string", "type": "apps"}]}
)
```

---

### 
> 

```python
client.v2.app_availabilities.create(
    data={
        "data": {
            "attributes": {"available_in_new_territories": True},
            "relationships": {
                "app": {"data": {"id": "string", "type": "apps"}},
                "territory_availabilities": {
                    "data": [{"id": "string", "type": "territoryAvailabilities"}]
                },
            },
            "type": "appAvailabilities",
        },
        "included": [{"id": "string", "type": "territoryAvailabilities"}],
    }
)
```

---

### 
> 

```python
client.v2.app_store_version_experiments.create(
    data={
        "data": {
            "attributes": {
                "name": "string",
                "platform_field": "IOS",
                "traffic_proportion": 123,
            },
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "appStoreVersionExperiments",
        }
    }
)
```

---

### 
> 

```python
client.v2.in_app_purchases.create(
    data={
        "data": {
            "attributes": {
                "family_sharable": True,
                "in_app_purchase_type": "CONSUMABLE",
                "name": "string",
                "product_id": "string",
                "review_note": "string",
            },
            "relationships": {"app": {"data": {"id": "string", "type": "apps"}}},
            "type": "inAppPurchases",
        }
    }
)
```

---

### 
> 

```python
client.v2.sandbox_testers_clear_purchase_history_request.create(
    data={
        "data": {
            "relationships": {
                "sandbox_testers": {
                    "data": [{"id": "string", "type": "sandboxTesters"}]
                }
            },
            "type": "sandboxTestersClearPurchaseHistoryRequest",
        }
    }
)
```


