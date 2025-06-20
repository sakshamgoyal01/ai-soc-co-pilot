from kubernetes import client, config
config.load_kube_config()

def isolate_pod(pod_name, namespace="default"):
    api = client.CoreV1Api()
    api.patch_namespaced_pod(
        name=pod_name,
        namespace=namespace,
        body={"metadata": {"labels": {"isolated": "true"}}}
    )

def restart_service(service_name, namespace="default"):
    apps = client.AppsV1Api()
    apps.patch_namespaced_deployment(
        name=service_name,
        namespace=namespace,
        body={"spec": {"template": {"metadata": {"annotations": {"kubectl.kubernetes.io/restartedAt": "now"}}}}}
    )
