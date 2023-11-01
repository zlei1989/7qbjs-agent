from modelscope import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "damo/ModelScope-Agent-7B", revision='v1.0.0', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("damo/ModelScope-Agent-7B", revision='v1.0.0',
                                             device_map="auto", trust_remote_code=True, fp16=True).eval()


system = """
 <|system|>:当前对话可以使用的插件信息如下，请自行判断是否需要调用插件来解决当前用户问题。若需要调用插件，则需要将插件调用请求按
照json格式给出，必须包含api_name、url、parameters字段，并在其前后使用<|startofthink|>和<|endofthink|>作为标志。然后你需要根据插
件API调用结果生成合理的答复；若无需调用插件，则直接给出对应回复即可：

1. {"name": "NewPage", "description": "创建新页面", "parameters": [{"name": "pageTitle", "description": "页面标题", "required": true},{"name": "pagePath","description": "页面路径。不指定则把标题翻译成英文，全小写，英文单词间用减号隔开，如商户信息的是merchant-information）","required":true}]}
"""

response, history = model.chat(tokenizer, "帮我创建一个表单页面，标题是商户入住。", history=None, system=system)
print(response)
