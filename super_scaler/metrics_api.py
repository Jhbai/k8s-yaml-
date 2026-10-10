# main.py
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/apis/external.metrics.k8s.io/v1beta1")
def get_external_api_info():
    # 必須提供該 API Group 的 Discovery 資訊
    return {
        "kind": "APIResourceList",
        "apiVersion": "v1",
        "groupVersion": "external.metrics.k8s.io/v1beta1",
        "resources": [
            {
                "name": "my_custom_queue_depth",
                "singularName": "",
                "namespaced": False,
                "kind": "ExternalMetricValueList",
                "verbs": ["get"]
            }
        ]
    }

@app.get("/apis/external.metrics.k8s.io/v1beta1/{metric_name}")
def get_metric(metric_name: str):
    # 這裡放你的業務計算邏輯或向後端資料庫取得指標數值
    current_value = 150  # 範例數值
    
    return {
        "kind": "ExternalMetricValueList",
        "apiVersion": "external.metrics.k8s.io/v1beta1",
        "metadata": {},
        "items": [
            {
                "metricName": metric_name,
                "metricLabels": {},
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "value": f"{current_value}" # K8s 偏好傳遞字串格式整數/帶單位值
            }
        ]
    }
