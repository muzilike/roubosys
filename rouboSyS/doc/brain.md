# 调度中心设计和需求记录

## 职责

    实时调度所有jobs，SuperCmdLine实时控制所有jobs，获取所有job的运行信息。
    每个job都是以进程方式被调度，需要被命名，可调度的所有jobs与调度中心无耦合。
    每个job只有一个可调度入口，每个入口通过import方式导入，因此可以有一个统一的jobs入口。
    如何实现动态加载新编写的job？暂不实现。

## 实现第一个demo job的调度，reload，start，stop

    需要支持从brain直接运行整个jobs列表，使用通配符‘#’作为name的传入参数。
    需要支持从brain直接运行当个job，参数为name，也就是唯一的job name。
    也就是说，需要在roubosysjobs中实现一个通过name来返回可调度fun或者funs列表。

## Brain管理下的super cmd line机制

    super cmd line(简称SCL), 作为一个独立的job运行，但是由于他可以操作所有其他jobs。
    SML需要登录进入，需要支持本地和远程登录，所以他的鉴权机制使用socket实现
    SML job作为一个server运行在brain中，client就是管理员的登录程序。
    SML鉴权可以在client的配合下，实现passwd，key。甚至是人脸之类的的识别机制。
    admin登录之后，使用循环显示jobs状态信息的默认方式，并且允许事件中断
    设计一套交互命令
    紧急事件允许紧急呈现
 
