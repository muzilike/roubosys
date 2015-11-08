# 可调度任务设计和需求记录

## 利用Fitbit flex来实现roubosys和admin的沟通

    研究Fitbit flex apis：https://wiki.fitbit.com/display/API/Fitbit+API
    实现一个消息通知的通道，可被brain使用，用于发布紧急或日常消息

### Fitbit OAuth

    Fitbit API使用了OAuth 1.0a来授权，Fitbit 本身提供了python api，在使用时注意OAuth认证流程
