from api_classes.api_caller import ApiCaller


class ApiEnvironments(ApiCaller):
    endpoint_url = '/api/environments'
    request_method_name = ApiCaller.CONST_REQUEST_METHOD_GET
    endpoint_auth_level = ApiCaller.CONST_API_AUTH_LEVEL_RESTRICTED
