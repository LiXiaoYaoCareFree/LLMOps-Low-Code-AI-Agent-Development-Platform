import random

from langchain_core.runnables import RunnableLambda


def get_weather(location: str, unit: str, name: str) -> str:
    """根据传入的位置+温度单位获取对应的天气信息"""
    print("location:", location)
    print("unit:", unit)
    print("name:", name)
    return f"{location}天气为{random.randint(24, 40)}{unit}"


get_weather_runnable = RunnableLambda(get_weather).bind(unit="摄氏度", name="lly")

resp = get_weather_runnable.invoke("广州")

print(resp)
