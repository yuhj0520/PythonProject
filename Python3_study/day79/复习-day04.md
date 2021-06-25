

## 1 Django与Ajax

```python
# 通过ajax向https://api.help.bj.cn/apis/life29/?id=101060101发送请求，看看能不能拿回数据

一 什么是Ajax
二 基于jquery的Ajax实现
三 案例
四 文件上传
五 Ajax提交json格式数据
六 Django内置的serializers（把对象序列化成json字符串）
```



## 2分页器组件

```python
固定代码，修改就可以
```



## 3 **forms组件**

```python
1 使用它字段校验功能
	-1 写一个类（UserForm），继承Form
    -2 在类中写字段，pwd=forms.CharField(max_length=32,min_length=4)
    -3 在视图函数中使用：form=UserForm(校验的字典)
    -4 form.is_valid() 通过了，就可以存起来，不通过，form.errors会有错误信息
2 默认的校验规则还不够，需要自己写钩子函数
	-局部钩子：
    	def clean_字段名()
        	val=self.cleaned_data.get("name") # val就是要校验的字段，做限制
            通过直接return
            不通过抛出raise ValidationError("该用户已注册!")
    -全局钩子：
    	    def clean(self):
                pwd=self.cleaned_data.get('pwd')
                r_pwd=self.cleaned_data.get('r_pwd')

                if pwd and r_pwd:
                    if pwd==r_pwd:
                        return self.cleaned_data
                    else:
                        raise ValidationError('两次密码不一致')
                else:

                    return self.cleaned_data
                
 # forms组件源码执行流程
	form.is_valid()----》内部起了一个for循环，先去校验每个字段配置的规则，校验完成，走该字段的局部钩子函数，一个一个执行完（交验完）---》会走全局钩子（clean()）--->self就会有clean_data和errors
    
1 流程：
	1 form.is_valid()
    2 self.errors
    3 self.full_clean()
    4   self._clean_fields()   局部字段的校验（自己的和局部钩子）
    		    if hasattr(self, 'clean_%s' % name):
                    func=getattr(self, 'clean_%s' % name)
                    value = func()
                    self.cleaned_data[name] = value
        self._clean_form()     全局的钩子
        self._post_clean()
        
        

```



## 4cookie与session组件

```python
# 使用django放置cookie
response.set_cookie(key,value)   （HttpResonse对象） render，JsonResponse，redirect
response.set_signed_cookie(key,value,salt='加密盐')
# 参数详解
key, 键
value='', 值
max_age=None, 超时时间 cookie需要延续的时间（以秒为单位）如果参数是\ None`` ，这个cookie会延续到浏览器关闭为止
expires=None, 超时时间(IE requires expires, so set it if hasn't been already.)
path='/', Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问，浏览器只会把cookie回传给带有该路径的页面，这样可以避免将cookie传给站点中的其他的应用。
domain=None, Cookie生效的域名 你可用这个参数来构造一个跨站cookie。如， domain=".example.com"所构造的cookie对下面这些站点都是可读的：www.example.com 、 www2.example.com 和an.other.sub.domain.example.com 。如果该参数设置为 None ，cookie只能由设置它的站点读取
secure=False, 浏览器将通过HTTPS来回传cookie
httponly=False 只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
# 删除cookie 
response.delete_cookie("user")

# 获取cookie
request.COOKIES['key']    # request对象
request.COOKIES.get('key')
```

```python
#设置session
# 获取、设置、删除Session中数据
request.session['k1']
request.session.get('k1',None)
request.session['k1'] = 123
request.session.setdefault('k1',123) # 存在则不设置
del request.session['k1']


# 所有 键、值、键值对
request.session.keys()
request.session.values()
request.session.items()
request.session.iterkeys()
request.session.itervalues()
request.session.iteritems()

# 会话session的key
request.session.session_key

# 将所有Session失效日期小于当前日期的数据删除
request.session.clear_expired()

# 检查会话session的key在数据库中是否存在
request.session.exists("session_key")

# 删除当前会话的所有Session数据(只删数据库)
request.session.delete()
　　
# 删除当前的会话数据并删除会话的Cookie（数据库和cookie都删）。
request.session.flush() 
    这用于确保前面的会话数据不可以再次被用户的浏览器访问
    例如，django.contrib.auth.logout() 函数中就会调用它。

# 设置会话Session和Cookie的超时时间
request.session.set_expiry(value)
    * 如果value是个整数，session会在些秒数后失效。
    * 如果value是个datatime或timedelta，session就会在这个时间后失效。
    * 如果value是0,用户关闭浏览器session就会失效。
    * 如果value是None,session会依赖全局session失效策略。
```



## 5中间件组件 

```python
process_request(self,request)
	return response(不再往后走，直接就回去了)
	return None  会继续往后走
process_response(self, request, response)
	
	return response（否则报错）

# 进来的时候，从上往下执行
# 出的时候，从下往上
```



## 6Auth模块

```python
# 记住这些
authenticate()
login(HttpRequest, user)
logout(request)
is_authenticated()
login_requierd()
create_user()
create_superuser()
check_password(password)
set_password(password)

#扩展auth_user表
自己写一个类，继承AbstractUser，自己写扩展字段
在setting中配置：AUTH_USER_MODEL = "app名.UserInfo"
```



## 作业：

1 学的不好的同学：用ajax提交一个json格式数据，返回一个json格式数据，console.log打印出来

2 通过ajax上传一个文件并保存起来，前端接收到，弹窗说上传成功



3 大家都写的：

用ajax提交用户的注册信息（用户名，密码，确认密码，年龄）（json），form组件做认证，姓名要大于4，小于16，不能以sb开头和结尾，用户名如果存在，也不能存进去，密码（最大16位，最小4位），年龄，小于150，大于18岁，密码和确认密码要一致，校验通过，存到user表中，

4 读一下forms执行流程



5 自己手动实现一个存文件的session，自定制一个session字典

6 敲一遍bbs项目

