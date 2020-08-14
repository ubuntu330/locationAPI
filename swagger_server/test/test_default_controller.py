# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_tracking_subscription import UserTrackingSubscription  # noqa: E501
from swagger_server.models.zonal_traffic_subscription import ZonalTrafficSubscription  # noqa: E501
from swagger_server.models.zone_status_subscription import ZoneStatusSubscription  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_subscriptions_user_tracking_get(self):
        """Test case for subscriptions_user_tracking_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/userTracking',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_user_tracking_post(self):
        """Test case for subscriptions_user_tracking_post

        
        """
        userTrackingSubscription = UserTrackingSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/userTracking',
            method='POST',
            data=json.dumps(userTrackingSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_user_tracking_subscription_id_delete(self):
        """Test case for subscriptions_user_tracking_subscription_id_delete

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/userTracking/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_user_tracking_subscription_id_get(self):
        """Test case for subscriptions_user_tracking_subscription_id_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/userTracking/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_user_tracking_subscription_id_put(self):
        """Test case for subscriptions_user_tracking_subscription_id_put

        
        """
        userTrackingSubscription = UserTrackingSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/userTracking/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(userTrackingSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_status_get(self):
        """Test case for subscriptions_zonal_status_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalStatus',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_status_post(self):
        """Test case for subscriptions_zonal_status_post

        
        """
        zoneStatusSubscription = ZoneStatusSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalStatus',
            method='POST',
            data=json.dumps(zoneStatusSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_traffic_get(self):
        """Test case for subscriptions_zonal_traffic_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalTraffic',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_traffic_post(self):
        """Test case for subscriptions_zonal_traffic_post

        
        """
        zonalTrafficSubscription = ZonalTrafficSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalTraffic',
            method='POST',
            data=json.dumps(zonalTrafficSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_traffic_subscription_id_delete(self):
        """Test case for subscriptions_zonal_traffic_subscription_id_delete

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalTraffic/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_traffic_subscription_id_get(self):
        """Test case for subscriptions_zonal_traffic_subscription_id_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalTraffic/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zonal_traffic_subscription_id_put(self):
        """Test case for subscriptions_zonal_traffic_subscription_id_put

        
        """
        zonalTrafficSubscription = ZonalTrafficSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zonalTraffic/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(zonalTrafficSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zone_status_subscription_id_delete(self):
        """Test case for subscriptions_zone_status_subscription_id_delete

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zoneStatus/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zone_status_subscription_id_get(self):
        """Test case for subscriptions_zone_status_subscription_id_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zoneStatus/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subscriptions_zone_status_subscription_id_put(self):
        """Test case for subscriptions_zone_status_subscription_id_put

        
        """
        zoneStatusSubscription = ZoneStatusSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1//subscriptions/zoneStatus/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(zoneStatusSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        
        """
        query_string = [('zoneId', 'zoneId_example'),
                        ('accessPointId', 'accessPointId_example')]
        response = self.client.open(
            '/exampleAPI/location/v1//users',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//users/{userId}'.format(userId='userId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_get(self):
        """Test case for zones_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//zones',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_zone_id_access_points_access_point_id_get(self):
        """Test case for zones_zone_id_access_points_access_point_id_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//zones/{zoneId}/accessPoints/{accessPointId}'.format(zoneId='zoneId_example', accessPointId='accessPointId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_zone_id_access_points_get(self):
        """Test case for zones_zone_id_access_points_get

        
        """
        query_string = [('interestRealm', 'interestRealm_example')]
        response = self.client.open(
            '/exampleAPI/location/v1//zones/{zoneId}/accessPoints'.format(zoneId='zoneId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_zone_id_get(self):
        """Test case for zones_zone_id_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1//zones/{zoneId}'.format(zoneId='zoneId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
