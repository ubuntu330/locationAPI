import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_tracking_subscription import UserTrackingSubscription  # noqa: E501
from swagger_server.models.zonal_traffic_subscription import ZonalTrafficSubscription  # noqa: E501
from swagger_server.models.zone_status_subscription import ZoneStatusSubscription  # noqa: E501
from swagger_server import util


def subscriptions_user_tracking_get():  # noqa: E501
    """subscriptions_user_tracking_get

    This operation is used for retrieving all active subscriptions to user tracking change notifications. # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def subscriptions_user_tracking_post(userTrackingSubscription):  # noqa: E501
    """subscriptions_user_tracking_post

    This operation is used for creating a new subscription to user tracking change notification # noqa: E501

    :param userTrackingSubscription: User Tracking Subscription
    :type userTrackingSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        userTrackingSubscription = UserTrackingSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def subscriptions_user_tracking_subscription_id_delete(subscriptionId):  # noqa: E501
    """subscriptions_user_tracking_subscription_id_delete

    This operation is used for retrieving an individual subscription to user tracking change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def subscriptions_user_tracking_subscription_id_get(subscriptionId):  # noqa: E501
    """subscriptions_user_tracking_subscription_id_get

    This operation is used for retrieving an individual subscription to user tracking change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: object
    """
    return 'do some magic!'


def subscriptions_user_tracking_subscription_id_put(subscriptionId, userTrackingSubscription):  # noqa: E501
    """subscriptions_user_tracking_subscription_id_put

    This operation is used for updating an individual subscription to user tracking change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str
    :param userTrackingSubscription: User Tracking Subscription
    :type userTrackingSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        userTrackingSubscription = UserTrackingSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def subscriptions_zonal_status_get():  # noqa: E501
    """subscriptions_zonal_status_get

    This operation is used for creating a new subscription to zone status change notification. # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def subscriptions_zonal_status_post(zoneStatusSubscription):  # noqa: E501
    """subscriptions_zonal_status_post

    This operation is used for creating a new subscription to zone status change notification. # noqa: E501

    :param zoneStatusSubscription: Zone Status Subscription
    :type zoneStatusSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zoneStatusSubscription = ZoneStatusSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def subscriptions_zonal_traffic_get():  # noqa: E501
    """subscriptions_zonal_traffic_get

    This operation is used for retrieving all active subscriptions to zonal traffic change notifications. # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def subscriptions_zonal_traffic_post(zonalTrafficSubscription):  # noqa: E501
    """subscriptions_zonal_traffic_post

    This operation is used for creating a new subscription to zonal traffic change notification. # noqa: E501

    :param zonalTrafficSubscription: Zonal Traffic Subscription
    :type zonalTrafficSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zonalTrafficSubscription = ZonalTrafficSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def subscriptions_zonal_traffic_subscription_id_delete(subscriptionId):  # noqa: E501
    """subscriptions_zonal_traffic_subscription_id_delete

    This operation is used for cancelling a subscription and stopping corresponding notifications. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def subscriptions_zonal_traffic_subscription_id_get(subscriptionId):  # noqa: E501
    """subscriptions_zonal_traffic_subscription_id_get

    This operation is used for updating an individual subscription to zonal traffic change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: object
    """
    return 'do some magic!'


def subscriptions_zonal_traffic_subscription_id_put(subscriptionId, zonalTrafficSubscription):  # noqa: E501
    """subscriptions_zonal_traffic_subscription_id_put

    This operation is used for updating an individual subscription to zonal traffic change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str
    :param zonalTrafficSubscription: Zonal Traffic Subscription
    :type zonalTrafficSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zonalTrafficSubscription = ZonalTrafficSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def subscriptions_zone_status_subscription_id_delete(subscriptionId):  # noqa: E501
    """subscriptions_zone_status_subscription_id_delete

    This operation is used for cancelling a subscription and stopping corresponding notifications. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def subscriptions_zone_status_subscription_id_get(subscriptionId):  # noqa: E501
    """subscriptions_zone_status_subscription_id_get

    This operation is used for retrieving an individual subscription to zone status change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: object
    """
    return 'do some magic!'


def subscriptions_zone_status_subscription_id_put(subscriptionId, zoneStatusSubscription):  # noqa: E501
    """subscriptions_zone_status_subscription_id_put

    This operation is used for updating an individual subscription to zone status change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str
    :param zoneStatusSubscription: Zone Status Subscription
    :type zoneStatusSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zoneStatusSubscription = ZoneStatusSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_get(zoneId, accessPointId=None):  # noqa: E501
    """users_get

    Users currently using a zone may be retrieved for sets of access points matching attribute in the request # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str
    :param accessPointId: Identifier of access point, reference \&quot;definitions\&quot; for string format
    :type accessPointId: str

    :rtype: object
    """
    return 'do some magic!'


def users_user_id_get(userId):  # noqa: E501
    """users_user_id_get

    Users currently using a zone may be retrieved for sets of access points matching attribute in the request # noqa: E501

    :param userId: User ID
    :type userId: str

    :rtype: object
    """
    return 'do some magic!'


def zones_get():  # noqa: E501
    """zones_get

    Used to get a list of identifiers for zones authorized for use by the application. # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def zones_zone_id_access_points_access_point_id_get(zoneId, accessPointId):  # noqa: E501
    """zones_zone_id_access_points_access_point_id_get

    Access point status can be retrieved for sets of access points matching attribute in the request. # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str
    :param accessPointId: Access Point ID
    :type accessPointId: str

    :rtype: object
    """
    return 'do some magic!'


def zones_zone_id_access_points_get(zoneId, interestRealm=None):  # noqa: E501
    """zones_zone_id_access_points_get

    Access point status can be retrieved for sets of access points matching attribute in the request. # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str
    :param interestRealm: Interest realm of access point (e.g. geographical area, a type of industry etc.).
    :type interestRealm: str

    :rtype: object
    """
    return 'do some magic!'


def zones_zone_id_get(zoneId):  # noqa: E501
    """zones_zone_id_get

    Used to get the status of a zone. # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str

    :rtype: object
    """
    return 'do some magic!'
