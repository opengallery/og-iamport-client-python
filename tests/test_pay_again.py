import time


def test_pay_again(iamport):
    # Without 'customer_uid'
    payload_not_enough = {
        'merchant_uid': 'pay_again_muid_{}'.format(str(time.time())),
        'amount': 5000,
    }

    try:
        iamport.pay_again(**payload_not_enough)
    except KeyError as e:
        assert 'Essential parameter is missing!: customer_uid' in str(e)

    payload_full = {
        'customer_uid': 'pay_again_cuid_{}'.format(str(time.time())),
        'merchant_uid': 'pay_again_muid_{}'.format(str(time.time())),
        'amount': 5000,
    }

    try:
        iamport.pay_again(**payload_full)
    except iamport.ResponseError as e:
        assert e.code == 1
        assert u'등록되지 않은 구매자입니다.' in e.message
