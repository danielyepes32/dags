task_http_sensor_check = HttpSensor(
    task_id="run_hop_pipeline",
    http_conn_id="http_default",
    endpoint="",
    request_params={},
    response_check=lambda response: "httpbin" in response.text,
    poke_interval=5,
    dag=dag,
)