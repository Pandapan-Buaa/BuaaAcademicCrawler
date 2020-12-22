def jwt_response_payload_handler(token,user=None,request=None):
    '''
    ＪＷＴ登录成功之后，自定义的返回数据的处理,
    :param token:
    :param user:
    :param request:
    :return:
    '''
    data = {
        'code': 20000,
        'message': 'Success',
        'data': {'token':token},
    }
    return data
