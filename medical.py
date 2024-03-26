# import os
# os.system("pip install -U erniebot -i https://mirrors.aliyun.com/pypi/simple/")
import erniebot 
import gradio as gr


def predict(accesstoken, content, dd):
    erniebot.api_type = "aistudio"
    # 获取用户token
    erniebot.access_token = accesstoken
    # 主promnt
    model = dd
    message = f"你是一名非常著名的医生，在医疗届可谓无所不能，可以通过我所描述的话来判断我所患上的病，包括但不限于偏头痛、感冒、胃痛、过敏等，请在回答时给出你的判断依据，并且给出用药参考并予以适当警告，下面是我要查询的病症：病症描述 {content}"
    response = erniebot.ChatCompletion.create(model=model, messages=[{"role": "user",
                                                                            "content": message}])
    print(response.result)
    return response.result

with gr.Blocks(theme=gr.themes.Glass()) as demo:
    with gr.Row():
        gr.HTML(
            """<h1 align="center">赛博问诊</h1>""")
    with gr.Row():
        gr.HTML(
            """<img align="center" src='https://ziyuan.guwendao.net/siteimg/24jie/%e5%af%92%e9%9c%b2.jpg' width='100%'> <br>""")
    with gr.Row():
        gr.HTML(
            """<h3 align="center">请在描述框中输入您所想问的病情，越详细越好，各种病症最好分点列出。</h3>""")
    # token
    with gr.Row():
        accesstoken = gr.Textbox(label="请输入您的token，它看起来像这样：asd6587afa13efawf**********", interactive=True)
    # promnt
    with gr.Row():
        input = gr.Textbox(label="描述", interactive=True, )
    # 
    with gr.Row():
        dd = gr.Dropdown(label="模型", value="ernie-3.5", allow_custom_value=True,
                          choices=["ernie-3.5", "ernie-turbo", "ernie-4.0", "ernie-longtext"])

    with gr.Row():
        btn1 = gr.Button("🚀一键问诊🚀")
        btn2 = gr.Button("✨药到病除✨")

    with gr.Row():
        output = gr.Textbox(lines=20, label='输出（推理需要时间，请耐心等待）')
        btn1.click(fn=predict, inputs=[accesstoken, input, dd], outputs=output)
        btn2.click(lambda _: (None, None, None), inputs=btn2, outputs=[input])

demo.launch()
