import sys
sys.path.append('../modelscope-agent/')

from modelscope_agent.llm import LLMFactory
from modelscope.hub.api import HubApi

model_name = 'modelscope-agent-7b'
model_cfg = {
    'modelscope-agent-7b':{
        'type': 'modelscope',
        'model_id': 'damo/ModelScope-Agent-7B',
        'model_revision': 'v1.0.0',
        'use_raw_generation_config': True,
        'custom_chat': True
    }
}


llm = LLMFactory.build_llm(model_name, model_cfg)

from modelscope_agent.agent import AgentExecutor
from modelscope_agent.tools import Tool

class QqbNewPageTool(Tool):
    description = '创建一个页面'
    name = 'NewPage'
    parameters: list = [{
        'name': 'pageTitle',
        'description': '页面的标题',
        'required': True
    }, {
        'name': 'pagePath',
        'description': '页面路径。不指定则把标题翻译成英文，全小写，英文单词间用减号隔开，如商户信息的是merchant-information',
        'required': True
    }]

    def _local_call(self, *args, **kwargs):
        pageTitle = kwargs['pageTitle']
        pagePath = kwargs['pagePath']
        return {'result': f'创建页面《{pageTitle}》成功，路径是{pagePath}'}

# 新增工具可参考AliyunRenewInstanceTool构建方式，配置相关的api name，description等
additional_tool_list = {
    'NewPage': QqbNewPageTool()
}
# 构建Agent，需要传入llm，工具配置config以及工具检索

agent = AgentExecutor(llm, additional_tool_list=additional_tool_list, tool_retrieval=False)
available_tool_list = ['NewPage']
agent.set_available_tools(available_tool_list)


# 重置对话，清空对话历史
agent.reset()

# remote=True为调用modelscope api，该服务免费支持QPS较低，建议部署在本地，将remote=False
agent.run("帮我创建一个表单页面，标题是商户入住", remote=False, print_info=True)