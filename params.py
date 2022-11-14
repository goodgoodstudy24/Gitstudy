import pytest


# params参数：设置参数化
# @pytest.fixture(params=["jack", "rose", "jimmy"])
# def fixture1(request):
#     print(request.param) # request.param的值为参数化中的数据的其中一个值
#     print("测试用例前置步骤")
#     return request.param # 将参数化的数据依次返回
#
#
# @pytest.fixture(params=[("admin","123456"), ("root", "567890")])
# def fixture2(request):
#     print("测试用例前置步骤一, 用户名：", request.param)
#     yield request.param # 通过yield将参数化的数据传递给test开头的函数（测试用例）
#     print("测试用例后置步骤一")
#
#
# def test001(fixture1): # test001执行次数为参数化的数据的元素数量
#     print("使用requests进行接口请求，使用用户名：", fixture1) # fixture1的值为其返回值
#
# def test002(fixture2):
#     print("测试连接数据库，使用用户名：%s, 密码：%s" % fixture2)

# @pytest.fixture()
# def fixture3(params): # fixture函数的参数名称，与parametrize第一个参数的值要对应
#     print("前置步骤获取参数化数据：", params)
#
# # pytest.mark.paramtrize(test开头的参数名称, 参数化数据)
# @pytest.mark.parametrize("account", ["jack", "rose"])
# def test001(account): # account参数要与parametrize的第一个参数对应
#     print("用户名：%s" % account)
#
# params=[("jack", "123456"), ("rose", "244750")]
#
# @pytest.mark.parametrize("params", [("jack", "123456"), ("rose", "244750")])
# def test002(params, fixture3):
#     print("用户名: %s, 密码：%s" % params)
#
# # test函数需要设置多个参数名称，parametrize第一个参数里使用逗号，分隔
# @pytest.mark.parametrize("user, passwd", [("admin", "123456"), ("root", "root1234")])
# def test003(user, passwd):
#     print("用户名：%s, 密码：%s" % (user, passwd))
#
# @pytest.mark.parametrize("user", ["admin", "root"])
# @pytest.mark.parametrize("passwd", ["123456", "167890"])
# def test004(user, passwd):
#     print("用户名：%s, 密码：%s" % (user, passwd)
