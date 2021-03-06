import time


def test_customer_get(iamport):
    customer_uid = 'customer_get_cuid_{}'.format(str(time.time()))
    try:
        iamport.customer_get(customer_uid)
    except iamport.ResponseError as e:
        assert e.code == 1
        assert e.message == u'요청하신 customer_uid({})로 등록된 정보를 찾을 수 없습니다.'.format(customer_uid)
